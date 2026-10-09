from pathlib import Path
import re
import struct
import subprocess

BINARY = (
    Path(__file__).resolve().parents[1]
    / "player" / "exfil_tool.elf"
)

# Address identified from this build's disassembly.
TARGET_ADDRESS = 0x487020
KEY_LENGTH = 17


def read_virtual_bytes(data, address, length):
    # ELF64, little-endian.
    if data[:6] != b"\x7fELF\x02\x01":
        raise ValueError("Expected a little-endian ELF64 binary.")

    ph_offset = struct.unpack_from("<Q", data, 32)[0]
    ph_size = struct.unpack_from("<H", data, 54)[0]
    ph_count = struct.unpack_from("<H", data, 56)[0]

    for i in range(ph_count):
        position = ph_offset + i * ph_size
        kind, flags, offset, virtual, physical, file_size, memory_size, align = (
            struct.unpack_from("<IIQQQQQQ", data, position)
        )

        if kind == 1 and (
            virtual <= address
            and address + length <= virtual + file_size
        ):
            start = offset + address - virtual
            result = data[start:start + length]
            if len(result) != length:
                raise ValueError("Truncated target table.")
            return result

    raise ValueError("Target address is not in a file-backed LOAD segment.")


def rotate_right_3(value):
    return ((value >> 3) | (value << 5)) & 0xff


def main():
    target = read_virtual_bytes(
        BINARY.read_bytes(), TARGET_ADDRESS, KEY_LENGTH
    )
    print("Target bytes:", target.hex())

    token = bytearray(KEY_LENGTH)

    for i, expected in enumerate(target):
        rotated = (expected - 17 * i - 0x29) & 0xff
        position = (i * 5) % KEY_LENGTH
        token[position] = rotate_right_3(rotated)

    recovered = token.decode("ascii")
    print("Recovered token:", recovered)

    result = subprocess.run(
        [str(BINARY), recovered],
        capture_output=True,
        text=True,
        check=True,
    )

    print("\nBinary output:")
    print(result.stdout)

    flag = re.search(r"NOVATECH\{[^}\r\n]+\}", result.stdout)
    if flag is None:
        raise SystemExit("Binary did not print a flag.")

    print("Recovered flag:", flag.group())


if __name__ == "__main__":
    main()

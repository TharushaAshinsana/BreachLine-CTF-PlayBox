#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define KEY_LEN 17

static const uint8_t target[KEY_LEN] = {
    0x9b, 0x65, 0xe4, 0xef, 0x78, 0xe7, 0x42, 0x21,
    0xcc, 0xdd, 0x9e, 0x86, 0x87, 0x31, 0xca, 0x6b,
    0xba
};

static const uint8_t encrypted_flag[] = {
    0x53, 0x25, 0x41, 0x48, 0x6f, 0x56, 0x5d, 0xa4,
    0xdd, 0xa2, 0xc3, 0xad, 0xf6, 0xaa, 0xa9, 0x91,
    0xd6, 0xeb, 0x86, 0xc7, 0xdd, 0xed, 0xfa, 0xf2,
    0xf0, 0x40, 0x2d, 0x46, 0x06, 0x4b, 0x37, 0x34
};

static uint8_t rotate_left_3(uint8_t value)
{
    return (uint8_t)((value << 3) | (value >> 5));
}

static int validate(const unsigned char *input)
{
    if (strlen((const char *)input) != KEY_LEN)
        return 0;

    uint8_t difference = 0;

    for (unsigned int i = 0; i < KEY_LEN; i++) {
        unsigned int position = (i * 5) % KEY_LEN;
        uint8_t transformed = (uint8_t)(
            rotate_left_3(input[position]) + 17 * i + 0x29
        );
        difference |= transformed ^ target[i];
    }

    return difference == 0;
}

static void reveal_flag(const unsigned char *input)
{
    for (unsigned int i = 0; i < sizeof(encrypted_flag); i++) {
        uint8_t mask = (uint8_t)(i * 7 + 0x53);
        putchar(encrypted_flag[i] ^ input[i % KEY_LEN] ^ mask);
    }
    putchar('\n');
}

int main(int argc, char **argv)
{
    puts("NovaTech recovered utility - offline analysis specimen");

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <recovery-token>\n", argv[0]);
        return 2;
    }

    const unsigned char *input = (const unsigned char *)argv[1];

    if (!validate(input)) {
        puts("Access denied.");
        return 1;
    }

    puts("Token accepted.");
    reveal_flag(input);
    return 0;
}

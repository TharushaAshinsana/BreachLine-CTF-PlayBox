
flowchart TD
    P["CTF Player / Browser"]
    A["Administrator"]
    N["Nginx Reverse Proxy :80"]

    C["CTFd Platform :8000"]
    R[("Redis :6379")]
    D[("CTFd MariaDB :3306")]

    W["Member 2: Flask Web Challenge :5000"]
    S[("Challenge MariaDB :3306")]

    P -->|"HTTP"| N
    A -->|"Admin access :8000"| C

    N -->|"Default website"| C
    N -->|"portal.novatech.local"| W
    N -->|"intra.novatech.local"| C

    C --> R
    C --> D
    W --> S

    subgraph CTF_NETWORK["CTF Network"]
        C
        R
        D
    end

    subgraph CHALLENGE_NETWORK["Isolated Challenge Network"]
        W
        S
    end
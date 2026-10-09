# BreachLine: The NovaTech Incident – CTF Play Box

## Project Overview

BreachLine is a Capture The Flag (CTF) cybersecurity training environment designed for practical security challenges.

## Member 1 – Platform Architecture and Deployment

My responsibility is to design the platform architecture and configure the deployment environment.

## Architecture Components

* **CTFd:** CTF platform for managing challenges and flag submissions.
* **Nginx:** Reverse proxy for routing HTTP requests.
* **MariaDB:** Database services for the platform and web challenge.
* **Redis:** Supporting service for CTFd.
* **Docker Compose:** Manages the containers and services.
* **Docker Networks:** Separate networks for the CTF platform and challenge environment.

See [`docs/architecture.md`](docs/architecture.md) for the architecture diagram.

## Requirements

* Docker Desktop
* Docker Compose
* Git

## Start the Environment

Run these commands in PowerShell from the project root:

```powershell
docker compose config --quiet
docker compose up -d
docker compose ps
```

## Access

* CTFd: http://localhost:8000
* Nginx entry point: http://localhost

## View Logs

```powershell
docker compose logs --tail=100
```

## Stop the Environment

```powershell
docker compose down
```

## Reset and Recovery

Restart services with:

```powershell
docker compose restart
```

**Warning:** `docker compose down -v` deletes named volumes and may erase saved database data. Only use it when a full reset is intended.

## Security Considerations

* Challenge containers do not publish their own host ports in the current configuration.
* The challenge network is configured as an internal Docker network.
* This environment is intended for a local educational lab, not direct public deployment.

## Implementation Status

The base platform configuration has been prepared. Challenge integration, flag validation and end-to-end testing must be verified before declaring the complete environment operational.

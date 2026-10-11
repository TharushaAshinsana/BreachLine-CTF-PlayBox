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

- Main CTF platform: http://localhost
- Nginx is the main entry point for web access.
- CTFd is accessed through Nginx and is not directly published on host port 8000.

## View Logs

```powershell
docker compose logs --tail=100
```

## Stop the Environment

```powershell
docker compose down
```

## Reset and Recovery


To restart all services:

    docker compose restart

To restart the S3 challenge web application:

    powershell -ExecutionPolicy Bypass -File .\challenges\member2\s3-point-of-entry\reset-s3.ps1

Note: The S3 recovery script restarts the S3 web container. It does not reset the challenge database or erase all challenge data.

Warning: Do not run docker compose down -v unless you intentionally want to delete the named volumes and their stored data.

## Security Considerations

* Challenge containers do not publish their own host ports in the current configuration.
* The challenge network is configured as an internal Docker network.
* This environment is intended for a local educational lab, not direct public deployment.

## Implementation Status

The Docker-based CTF platform and challenge services have been configured.

The integrated challenges should be tested through the browser, including challenge access and flag submission, before final submission.

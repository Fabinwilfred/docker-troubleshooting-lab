# Docker Troubleshooting Lab

A hands-on, scenario-based lab for practising Docker debugging with deliberately broken configurations.

## Prerequisites

- Docker Engine or Docker Desktop
- Docker Compose v2 (`docker compose version`)
- A terminal and `curl`

## How to use this lab

Every directory in `scenarios/` is self-contained. Read its `README.md`, start it with `docker compose up -d`, investigate, then apply the proposed fix yourself. The broken file is intentional—do not read the solution until you have tried.

```bash
cd scenarios/port-mapping
docker compose up -d
docker compose ps
```

Clean up after each exercise:

```bash
docker compose down -v
```

## Scenarios

| Scenario | Failure | Useful commands |
|---|---|---|
| [Container crash](scenarios/container-crash) | A process exits immediately | `docker logs`, `docker ps -a`, `docker inspect` |
| [Port mapping](scenarios/port-mapping) | Service is not reachable on the expected host port | `docker ps`, `docker port`, `curl` |
| [Networking](scenarios/networking) | Containers cannot resolve or reach one another | `docker network ls`, `docker network inspect`, `docker exec` |
| [Volumes](scenarios/volumes) | Data appears to disappear | `docker volume ls`, `docker exec`, `mount` |
| [Healthcheck](scenarios/healthcheck) | Container is running but unhealthy | `docker ps`, `docker inspect` |
| [Environment variables](scenarios/env-vars) | App starts with incorrect configuration | `docker exec env`, `docker inspect` |
| [Restart policy](scenarios/restart-policy) | Container does not restart after stopping | `docker events`, `docker inspect` |
| [Compose configuration](scenarios/compose) | Compose file resolves unexpected values | `docker compose config`, `docker compose up`, `docker compose down` |

## Recommended debugging flow

1. Check the state: `docker ps -a`
2. Read the logs: `docker logs <container>`
3. Inspect the exact configuration: `docker inspect <container>`
4. Test reachability: `curl localhost:<port>` or `docker exec <container> ...`
5. Inspect networks, volumes and resources when applicable.

## Nginx exits with code 0: a useful clue

An exit code of `0` normally means the process finished successfully, not that it crashed. Nginx shutdown logs ending in worker exits and `SIGQUIT` indicate a graceful shutdown. Common causes include `docker stop`, `docker compose down`, a Docker daemon restart, or a host reboot. If an Nginx service should return after a Docker restart, use a suitable restart policy such as:

```yaml
services:
  web:
    image: nginx:alpine
    restart: unless-stopped
```

Use `docker events --since "48h"` to investigate when it was stopped. On Linux hosts, Docker service logs can also help: `journalctl -u docker --since yesterday`.

## License

MIT. See [LICENSE](LICENSE).

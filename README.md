# Docker Troubleshooting Lab

A small hands-on lab for practising Docker troubleshooting methods. Each scenario deliberately contains a faulty Docker Compose configuration so you can investigate it, identify the cause, and apply the fix.

## What you can practise

- Checking container state and exit codes: `docker ps -a`, `docker inspect`
- Reading application logs: `docker logs`
- Diagnosing inaccessible services and incorrect port mappings: `docker port`, `curl`
- Checking container DNS and networks: `docker network inspect`, `docker exec`
- Verifying volumes and persistent data: `docker volume ls`, `mount`
- Finding incorrect environment variables and health checks
- Understanding restart policies and Compose variable resolution: `docker events`, `docker compose config`

## Run a scenario

```bash
cd scenarios/port-mapping
docker compose up -d
docker compose ps
```

Read the scenario `README.md`, investigate the intentional problem, and update `compose.yaml` to fix it. Then remove the lab resources:

```bash
docker compose down -v
```

## Why there are no Dockerfiles

The lab uses small public images such as `nginx:alpine` and `alpine:3.20`. This keeps the focus on debugging containers, networks, ports, volumes, configuration, and Compose rather than image-building.

## Requirements

- Docker Engine or Docker Desktop
- Docker Compose v2

MIT License. See [LICENSE](LICENSE).

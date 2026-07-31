# Docker Troubleshooting Lab

Hands-on, scenario-based Docker troubleshooting lab with deliberately broken configurations. This repository contains two complementary learning tracks so you can practice both focused single-issue debugging and multi-service investigation:

- Short scenarios: short, self-contained Compose projects each with one deliberate fault (easy to iterate and reset).
- Full-stack playground: a realistic multi-service stack (reverse proxy, frontend, API, workers, MySQL/Postgres, Redis, RabbitMQ, monitoring, logging) containing many intentional faults that require cross-service investigation.

## What you can practise

- Container state and exit codes: `docker ps -a`, `docker inspect`
- Application logs and startup problems: `docker logs`
- Ports and reachability: `docker port`, `curl`, host port mapping
- Networks and DNS: `docker network inspect`, `docker exec`, container-to-container name resolution
- Volumes and permissions: `docker volume ls`, `ls -l`, bind mount troubleshooting
- Environment variables, healthchecks, restart policies and compose config: `docker exec env`, `docker inspect`, `docker compose config`
- Resource limits and runtime metrics: `docker stats`
- Image build and Dockerfile issues: `docker build`, container entrypoint/command inspection
- Observability basics: Prometheus, Grafana, Elasticsearch/Kibana or Loki/Promtail + Grafana

## Repo structure (top level)

```
README.md                 # this file
LICENSE
docs/                     # extended docs and scenario authoring guides
scenarios/                # per-scenario exercises (short, single-bug)
  compose/
  container-crash/
  port-mapping/
  healthcheck/
  env-vars/
  restart-policy/
  volumes/
  full-stack/             # (new) full multi-service stack with many faults
solutions/                # (optional) canonical fixes and walkthroughs
examples/                 # example docker-compose files and reference stacks
```

## Short scenarios — how to run
Each scenario is a small Compose project. Example:

```bash
cd scenarios/port-mapping
docker compose up -d
docker compose ps
# Investigate with docker ps, docker logs, docker port, curl...
docker compose down -v
```

Read the scenario README in each folder for the symptom, investigation hints and the intended fix.

## Full-stack playground
Add/inspect the `scenarios/full-stack/compose.yaml` (or `examples/full-stack/docker-compose.yml`). This is a multi-service stack meant for more realistic troubleshooting: cross-service dependency, network, resource, and observability problems. Treat each fault as an exercise.

(Example full-stack compose is provided in `examples/full-stack/docker-compose.yml` in this branch.)

## Branch strategy
Keep `main` stable (working baseline). Create one branch per exercise so learners can reset easily:

- main
- scenario-01-container-crash
- scenario-02-port-not-accessible
- ...
- scenario-20-dns-resolution
- scenario-full-stack

## Scenario catalog (recommended)
Short / single-bug scenarios (each one branch/subfolder):
1. Wrong MySQL healthcheck credentials
2. Wrong published port (host:container mismatch)
3. API uses wrong service name (DNS/network misconfig)
4. Missing volume mount (bind vs named volume)
5. restart: "no" when expected to restart
6. Container exits immediately (bad CMD/ENTRYPOINT)
7. Wrong environment variable (DB host/user)
8. Missing network declaration (container isolated)
9. Nginx upstream misconfigured
10. Read-only volume where write required
11. File permission denied on bind mount
12. Memory limit too low (OOM)
13. CPU limit too low (starvation)
14. Healthcheck calls wrong endpoint/script missing
15. Dockerfile COPY path incorrect (build failure)
16. Wrong ENTRYPOINT vs CMD usage (unexpected behavior)
17. Compose dependency ordering causing race conditions
18. Corrupted bind mount contents
19. DNS resolution failure inside containers
20. Signal handling / graceful shutdown (SIGQUIT vs SIGTERM)

Full-stack (multi-fault) scenario:
- A 12–15 service stack (frontend, api, worker, mysql, postgres, redis, rabbitmq, nginx reverse-proxy, prometheus, grafana, elasticsearch, kibana, optional minio/mailhog) with 15–20 intentional problems distributed across services.

## Solutions
Keep solutions/ in the repo and either:
- include step-by-step fixes (one-per-branch) behind a separate `solutions` branch, or
- keep solution hints in text files and full fixes as separate commits or PRs.

## Requirements
- Docker Engine or Docker Desktop
- Docker Compose v2
- (Optional) Docker CLI knowledge for logs, inspect, exec, stats

MIT License. See LICENSE.

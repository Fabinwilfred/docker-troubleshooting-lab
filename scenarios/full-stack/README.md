# Full-stack troubleshooting scenario

This folder contains a multi-service full-stack playground intended for more realistic troubleshooting. The stack combines frontend, API, workers, databases, cache, message queue, reverse-proxy, monitoring and logging services.

How to run

```bash
cd scenarios/full-stack
# or cd examples/full-stack if you prefer the example path
docker compose -f ../../examples/full-stack/docker-compose.yml up -d
docker compose -f ../../examples/full-stack/docker-compose.yml ps
```

Investigate with the usual tools: `docker ps`, `docker logs <service>`, `docker inspect`, `docker exec -it <service> sh`, `docker network ls`, `docker network inspect`, `curl`, `docker stats`.

Intentional faults included (pick one to practice):
- Wrong MySQL healthcheck credentials (healthcheck fails even though service is up)
- Incorrect published host port for a service (host port != expected)
- API configured to use the wrong DNS name for the DB
- Missing volume or bind-mount (data not persisted)
- A service set to `restart: "no"` that should restart
- A container exits immediately because of a bad CMD/ENTRYPOINT
- Wrong environment variable values for DB username/password
- A service not attached to the correct network (cannot reach other services)
- Nginx upstream misconfigured (reverse-proxy cannot reach backend)
- Read-only volume where the app needs write access
- File permission denied errors on a bind mount
- Resource limits (memory/cpu) set too low causing failures
- Healthcheck pointing at the wrong endpoint/port
- Dockerfile COPY path errors when rebuilding images
- Race condition caused by service startup ordering

Suggested workflow
1. Run the stack and identify symptoms (container not running, 502 from Nginx, unhealthy status, etc.).
2. Use `docker logs` and `docker inspect` to collect evidence.
3. Narrow down to the misconfiguration (environment, port mapping, volume, network).
4. Make incremental changes to the compose file or supporting files to fix the issue and recreate the affected container(s).

Cleanup

```bash
# stop and remove containers and volumes if you used the examples path
docker compose -f ../../examples/full-stack/docker-compose.yml down -v
```

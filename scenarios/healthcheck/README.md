# Healthcheck

Start with `docker compose up -d`, wait about 20 seconds, and inspect the status:

```bash
docker ps
docker inspect lab-healthcheck --format '{{json .State.Health}}'
```

The web server is listening on the standard Nginx port, but the health check tests a different port. Correct the endpoint and verify that the status becomes `healthy`.

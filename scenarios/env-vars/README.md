# Environment variables

Run `docker compose up -d`, then inspect the running configuration:

```bash
docker exec lab-env-vars env
docker inspect lab-env-vars --format '{{json .Config.Env}}'
```

The application should use the development environment and `http://api:8080`. Correct the values in `compose.yaml`, recreate the container, and recheck them.

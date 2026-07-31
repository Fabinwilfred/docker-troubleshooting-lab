# Container crash

Start the scenario with `docker compose up -d`.

## Symptom

The `worker` container is not running.

## Investigate

```bash
docker compose ps -a
docker logs lab-container-crash
docker inspect lab-container-crash
```

Find the command that ends the process and change it so the worker remains alive. One simple practice fix is `command: ["sh", "-c", "while true; do sleep 3600; done"]`.

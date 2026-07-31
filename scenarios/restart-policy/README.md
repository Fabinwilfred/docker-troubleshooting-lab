# Restart policy

Bring it up, stop the container, then inspect it:

```bash
docker compose up -d
docker stop lab-restart-policy
docker inspect lab-restart-policy --format '{{json .HostConfig.RestartPolicy}}'
docker events --since 10m
```

For a service that should come back after an unexpected Docker restart, use `unless-stopped` (or `always` when that behavior is truly required). Recreate the service and test its behavior.

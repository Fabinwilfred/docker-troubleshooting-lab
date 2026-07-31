# Volumes

Start this scenario and inspect `/data` in both containers:

```bash
docker exec lab-volume-writer ls -la /data
docker exec lab-volume-reader ls -la /data
docker volume ls
```

The named volume is declared but not mounted. Mount `lab_data` at `/data` for both services and recreate the containers. Confirm the timestamp persists.

# Docker troubleshooting cheat sheet

```bash
# State and logs
docker ps -a
docker logs <container>
docker inspect <container>

# Runtime configuration
docker exec <container> env
docker port <container>
docker stats

# Networking and storage
docker network ls
docker network inspect <network>
docker volume ls
docker exec <container> mount

# Compose
docker compose config
docker compose ps
docker compose down -v
```

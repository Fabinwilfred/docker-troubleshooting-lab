# Port mapping

Start with `docker compose up -d` and try `curl http://localhost:8080`.

The service is healthy but unavailable where expected. Use:

```bash
docker ps
docker port lab-port-mapping
curl http://localhost:8081
```

Correct the Compose mapping so port `8080` on the host reaches Nginx on port `80`.

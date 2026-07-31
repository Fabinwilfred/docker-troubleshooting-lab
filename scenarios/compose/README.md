# Compose configuration

The documentation says the site should be available at port `8080`, but it is not.

```bash
docker compose config
docker compose up -d
docker compose ps
```

Identify where `WEB_PORT` is set and choose the intended configuration. Remember that Compose automatically reads a `.env` file in the project directory.

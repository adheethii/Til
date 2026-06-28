# Docker Volumes and Networking

**Date:** 2026-06-28

## Docker Volumes

Containers are ephemeral — data is lost when a container stops. Volumes persist data outside the container.

```
Without volume: Container stops → data gone 💥
With volume:    Container stops → data persists ✅
```

### Creating and Using Volumes

```bash
# Create a named volume
docker volume create my_data

# Run container with volume mounted
docker run -v my_data:/app/data my-api

# Mount a local folder (bind mount)
docker run -v /home/user/data:/app/data my-api
```

### In docker-compose.yml

```yaml
services:
  api:
    image: my-api
    volumes:
      - model_data:/app/models    # named volume
      - ./logs:/app/logs          # bind mount

volumes:
  model_data:
```

---

## Docker Networking

Containers are isolated — networking lets them communicate.

### Default Networks

```bash
# List networks
docker network ls

# bridge → default, containers on same host can communicate
# host   → container uses host machine's network
# none   → no network access
```

### Container-to-Container Communication

```yaml
# In docker-compose — services can reach each other by name
services:
  api:
    build: .
    environment:
      - DB_HOST=db      # 'db' is the service name below

  db:
    image: postgres:14
```

The `api` container connects to `db` container using hostname `db` — Docker handles DNS automatically.

### Create Custom Network

```bash
docker network create my_network

docker run --network my_network --name api my-api
docker run --network my_network --name db postgres
```

---

## Useful Commands

```bash
# Inspect volume
docker volume inspect my_data

# Remove unused volumes
docker volume prune

# Inspect network
docker network inspect bridge
```

---

## Key Takeaway

> Volumes persist data beyond a container's lifecycle — essential for databases and ML models. In Docker Compose, services communicate using their service names as hostnames — Docker's built-in DNS handles routing automatically.

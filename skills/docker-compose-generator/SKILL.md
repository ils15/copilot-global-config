---
name: docker-compose-generator
description: Generate production-ready docker-compose.yml files with best practices for networking, volumes, health checks, resource limits, and service dependencies. Supports multi-service architectures.
---

# Docker Compose Generator

Generate production-ready `docker-compose.yml` files following best practices.

## What This Skill Does

Creates complete Docker Compose configurations for:
- Multi-service applications
- Database integration (PostgreSQL, MySQL, Redis)
- Networking and service discovery
- Volume management and persistence
- Health checks and restart policies
- Environment variable management
- Resource limits and constraints

## When to Use This Skill

- Starting a new project with Docker
- Adding services to existing compose file
- Migrating from manual Docker commands
- Setting up development/production environments
- Orchestrating microservices
- Configuring databases, caches, queues

## Basic Structure

```yaml
version: '3.8'

services:
  service-name:
    image: image:tag
    # or
    build:
      context: ./path
      dockerfile: Dockerfile
    
    container_name: unique-name
    restart: unless-stopped
    
    ports:
      - "host:container"
    
    environment:
      - VAR_NAME=value
    
    volumes:
      - ./local:/container
      - named-volume:/data
    
    networks:
      - app-network
    
    depends_on:
      - other-service
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  app-network:
    driver: bridge

volumes:
  named-volume:
```

## Common Service Templates

### 1. Web Application (Python/FastAPI)

```yaml
services:
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: myapp-api
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - ./backend:/app
      - /app/__pycache__
    networks:
      - app-network
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2. PostgreSQL Database

```yaml
services:
  db:
    image: postgres:15-alpine
    container_name: myapp-db
    restart: unless-stopped
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres-data:
```

### 3. Redis Cache

```yaml
services:
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    restart: unless-stopped
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

volumes:
  redis-data:
```

### 4. Nginx Reverse Proxy

```yaml
services:
  nginx:
    image: nginx:alpine
    container_name: myapp-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
      - static-files:/usr/share/nginx/html
    networks:
      - app-network
    depends_on:
      - api
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  static-files:
```

### 5. Frontend (React/Next.js)

```yaml
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: production
    container_name: myapp-frontend
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://api:8000
      - NODE_ENV=production
    networks:
      - app-network
    depends_on:
      - api
```

## Complete Multi-Service Example

```yaml
version: '3.8'

services:
  # Database
  db:
    image: postgres:15-alpine
    container_name: myapp-db
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Cache
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Backend API
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: myapp-api
    restart: unless-stopped
    environment:
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      REDIS_URL: redis://cache:6379
      SECRET_KEY: ${SECRET_KEY}
    volumes:
      - ./backend:/app
      - /app/__pycache__
    networks:
      - backend
      - frontend
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Frontend
  web:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: myapp-web
    restart: unless-stopped
    environment:
      NEXT_PUBLIC_API_URL: http://api:8000
    networks:
      - frontend
    depends_on:
      - api

  # Nginx
  nginx:
    image: nginx:alpine
    container_name: myapp-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    networks:
      - frontend
    depends_on:
      - web
      - api

networks:
  backend:
    driver: bridge
  frontend:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
```

## Best Practices

### 1. Networks
```yaml
# Separate frontend and backend networks
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # No external access
```

### 2. Resource Limits
```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### 3. Environment Variables
```yaml
# Use .env file
environment:
  - DB_HOST=${DB_HOST}
  - DB_PORT=${DB_PORT}

# Or env_file
env_file:
  - .env
  - .env.local
```

### 4. Volume Best Practices
```yaml
volumes:
  # Named volume for persistence
  - db-data:/var/lib/postgresql/data
  
  # Bind mount for development
  - ./src:/app/src
  
  # Anonymous volume to prevent override
  - /app/node_modules
```

### 5. Health Checks
```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost/health || exit 1"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

### 6. Logging
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

## Common Patterns

### Development vs Production
```yaml
# docker-compose.yml (base)
services:
  api:
    build: ./backend
    environment:
      - NODE_ENV=production

---
# docker-compose.override.yml (development)
services:
  api:
    volumes:
      - ./backend:/app
    environment:
      - NODE_ENV=development
    command: npm run dev
```

### Multiple Compose Files
```bash
# Development
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## Commands Cheat Sheet

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f [service]

# Stop services
docker-compose down

# Rebuild images
docker-compose build

# Restart service
docker-compose restart [service]

# Execute command in service
docker-compose exec [service] [command]

# Scale services
docker-compose up -d --scale api=3

# Remove volumes
docker-compose down -v
```

## Troubleshooting

### Service Not Starting
```bash
# Check logs
docker-compose logs [service]

# Check container status
docker-compose ps

# Rebuild without cache
docker-compose build --no-cache [service]
```

### Network Issues
```bash
# Inspect network
docker network inspect [network-name]

# Test connectivity
docker-compose exec [service] ping [other-service]
```

### Volume Issues
```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect [volume-name]

# Remove all volumes
docker-compose down -v
```

## Anti-Patterns to Avoid

❌ Not using health checks
❌ Exposing all ports to host
❌ Hardcoding secrets in compose file
❌ Not setting restart policies
❌ Using `latest` tags
❌ Not defining networks
❌ Missing depends_on conditions
❌ No resource limits

## Reference

- Docker Compose Docs: https://docs.docker.com/compose/
- Compose File Spec: https://docs.docker.com/compose/compose-file/
- Best Practices: https://docs.docker.com/develop/dev-best-practices/

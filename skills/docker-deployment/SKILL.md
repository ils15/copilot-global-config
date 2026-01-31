---
name: docker-deployment
description: "Docker deployment best practices - multi-stage builds, health checks, CI/CD integration"
---

# Docker Deployment Skill

## Multi-Stage Dockerfile

```dockerfile
# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime (slim image)
FROM python:3.11-slim

WORKDIR /app

# Copy compiled dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app/ ./app

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Expose port
EXPOSE 8000

# Run
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

## Docker Compose

```yaml
version: '3.8'

services:
  api:
    build: ./api
    container_name: api-service
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
    networks:
      - app-network
    
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network
  
  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

volumes:
  db-data:

networks:
  app-network:
    driver: bridge
```

## CI/CD Integration

```yaml
# .github/workflows/docker-build.yml
name: Docker Build & Push

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Run tests in container
        run: docker run myapp:${{ github.sha }} pytest
      
      - name: Push to registry
        if: startsWith(github.ref, 'refs/tags')
        run: |
          docker tag myapp:${{ github.sha }} myapp:latest
          docker push myapp:latest
```

## Performance Optimization
- Use `.dockerignore` (like `.gitignore`)
- Minimal base images (alpine, slim)
- Multi-stage builds reduce size
- Cache layers efficiently
- Remove artifacts after build

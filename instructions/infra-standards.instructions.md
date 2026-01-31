---
description: "Infrastructure standards for Docker and deployment"
name: "Infrastructure Standards"
applyTo: "**/{Dockerfile,docker-compose.yml,*.yml,*.yaml}"
---

# Infrastructure Standards (Rá)

## Docker Images
- Use multi-stage builds
- Minimize image layers
- Non-root user (never RUN as root)
- Health checks (HEALTHCHECK instruction)
- Slim/Alpine bases onde possível

## Compose Files
- Service dependencies declared
- Resource limits (memory, cpu)
- Restart policies (unless-stopped)
- Named volumes para persistence
- Network configuration

## Environment Configuration
- Nunca hardcode secrets
- .env files para development
- Environment variables para production
- Separate configs: dev/staging/prod

## CI/CD
- Automated testing before deploy
- Build on every commit
- Deploy on tagged releases
- Staging environment como gate

## Monitoring
- Healthcheck endpoints
- Log aggregation
- Metrics collection
- Alerts para errors/timeouts

## Scaling
- Stateless containers
- Horizontal scaling support
- Load balancer configuration
- Database connection pooling

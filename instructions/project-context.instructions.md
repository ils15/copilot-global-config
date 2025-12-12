---
applyTo: '**'
description: 'Project-specific context for Ofertasdachina platform'
---

# Project Context - Ofertasdachina Platform

## **Platform Overview**

**Ofertasdachina** is a multi-agent platform for e-commerce deal aggregation and distribution across multiple channels (Telegram bots, web, social media). The system consists of distributed microservices that communicate via REST APIs and message queues.

**Core Purpose:**
- Aggregate deals from multiple e-commerce sources (AliExpress, MercadoLivre, Amazon)
- Process and enrich product information with AI (Google Gemini)
- Distribute content via Telegram bots and social media
- Provide web interfaces for browsing and managing offers

---

## 📍 **Critical Reference Documents**

Before implementing ANY changes, refer to these documents:

| Document | Purpose | Location |
|----------|---------|----------|
| **🏗️ Agent Architecture** | Complete microservices architecture (START HERE!) | `/home/admin/agents.md` |
| **🗂️ Project Structure Map** | Complete folder & Memory Bank mapping | `/home/admin/ofertasdachina/docs/memory-bank/PROJECT-STRUCTURE-MAP.md` |
| **🔌 Port Configuration** | All port allocations (BY SERVICE strategy) | `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/QUICK-REFERENCE-PORTS.md` |
| **🐳 Docker Compose** | Service orchestration reference | `/home/admin/ofertasdachina/docker-compose.yml` |
| **🏢 Infrastructure** | Traefik, networks, secrets, deployment | `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/` |

**⭐ Quick Start Workflow:**
1. Read `/home/admin/agents.md` for complete architecture overview
2. Consult `/docs/memory-bank/PROJECT-STRUCTURE-MAP.md` to find relevant Memory Bank
3. Check specific Memory Bank's `00-overview.md` for service details
4. Verify port allocation in `/docs/memory-bank-infrastructure/QUICK-REFERENCE-PORTS.md` before any networking changes

---

## **Technology Stack**

### **Backend Services**
- **Language:** Python 3.11
- **Web Framework:** FastAPI (async) + Flask/Gunicorn (legacy bots)
- **Async:** asyncio, aiohttp
- **Database:** MariaDB 11.2
- **Cache:** Redis 7.2
- **Message Queue:** RabbitMQ 3.13
- **AI:** Google Gemini API (2.5-flash-preview, 2.5-flash-lite-preview)

### **Frontend Services**
- **Language:** Node.js 18
- **Framework:** React 18
- **Build:** Vite
- **Styling:** TailwindCSS

### **Infrastructure**
- **Containerization:** Docker + Docker Compose
- **Reverse Proxy:** Traefik (with Let's Encrypt SSL)
- **Secrets Management:** Environment Variables (migrating to HashiCorp Vault)
- **VPS:** Linux-based (Ubuntu/Debian)
- **Domain:** ofertachina.cloud

---

## **System Architecture**

### **🐳 CRITICAL: Docker Compose Location**

**Docker Compose files are located in `services/applications/` directory:**

```
ofertasdachina/
└── services/
    └── applications/
        ├── ofertachina-api/
        │   └── docker-compose.yml
        ├── ofertachina-bots/
        │   └── docker-compose-multi-service.yml
        └── ofertachina-frontend/
            └── docker-compose.yml
```

**Commands MUST use this path:**
- ✅ `cd /home/admin/ofertasdachina/services/applications/ofertachina-api && docker-compose build`
- ❌ `cd /home/admin/ofertasdachina/repos/ofertachina-api && docker-compose build` (WRONG - repos don't have docker-compose)

**For bots specifically:**
- ✅ `cd /home/admin/ofertasdachina/services/applications/ofertachina-bots && docker-compose -f docker-compose-multi-service.yml up -d`

This is the authoritative location for all container orchestration.

### **Agent-Based Microservices**

The platform follows a distributed agent architecture. See `/home/admin/agents.md` for complete details.

**Core Agents:**
1. **API Agent** (`repos/ofertachina-api/`)
   - Port: 3001 (ext) / 8000 (int)
   - Central REST API
   - Database management
   - Business logic orchestration

2. **Bots Container** (`repos/ofertachina-bots/`)
   - Ports: 5002-5006 (ext) / 8002-8006 (int)
   - 4 Telegram bots (affiliate, aliexpress, ofertas, alertas)
   - Webhook-based processing (Flask + Gunicorn)
   - ModularBot template architecture
   - Routed via Traefik reverse proxy

3. **Social Agent** (`repos/ofertachina-social/`)
   - Port: 6001 (ext) / 8000 (int)
   - Social media integrations (Instagram, Facebook, Twitter)
   - Automated posting and monitoring

4. **Frontend Agent** (`repos/ofertachina-site/`)
   - Port: 3000
   - Main web interface
   - React-based SPA

5. **Impressão 3D Agent** (`repos/impressao3dbr/`)
   - Port: 4001 (ext) / 8000 (int)
   - 3D printing marketplace
   - STL/OBJ file processing

### **Port Allocation Strategy**

**⚠️ IMPORTANT**: Always refer to the official port allocation document!

**📍 Source of Truth**: `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/QUICK-REFERENCE-PORTS.md`

**Quick Summary** (BY SERVICE strategy):
- **OfertaChina Product**: 3000-3999 (Frontend 3000, API 3001, Redis 3379)
- **Impressão3D Product**: 4000-4999 (Frontend 4000, API 4001, Redis 4379)
- **Telegram Bots** (future): 5000-5999
- **Infrastructure**: 6000-6999 (MariaDB 6306, Redis 6379, RabbitMQ 6672-6673)
- **Traefik**: 80, 443, 8080 (dev)

**When defining ports, ALWAYS**:
1. Reference `/docs/memory-bank-infrastructure/QUICK-REFERENCE-PORTS.md` first
2. Never hardcode ports directly in configs
3. Use environment variables from docker-compose files
4. Update this document if port allocation changes

**Full details available in**: `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/QUICK-REFERENCE-PORTS.md`

---

## **Secrets Management**

### **Current Status: Environment Variables**

Secrets are currently managed via environment variables loaded from `.env` files in each service directory.

**Standard Pattern:**
- Each service has a `.env` file (not committed to git)
- Secrets loaded via `python-dotenv` package
- `.env.example` files document required variables
- Backup copies stored securely outside repository

### **Naming Convention**

| Type | Format | Example | Usage |
|------|--------|---------|-------|
| 🔵 **Internal API** | `*_INTERNAL_API_KEY` | `MASTER_INTERNAL_API_KEY` | Bot → API |
| 🟢 **Telegram** | `TELEGRAM_BOT_TOKEN_*` | `TELEGRAM_BOT_TOKEN_AFFILIATE` | Bot → Telegram |
| 🟡 **Security** | `*_SECRET`, `*_KEY` | `JWT_SECRET` | Crypto, sessions |
| 🟣 **External** | `*_API_KEY` | `GEMINI_API_KEY` | 3rd party services |

### **Secret Categories**

**Shared Infrastructure** (used by multiple services):
- `MARIADB_ROOT_PASSWORD`, `MARIADB_PASSWORD`, `MARIADB_USER`
- `REDIS_PASSWORD`
- `RABBITMQ_USER`, `RABBITMQ_PASSWORD`
- `GEMINI_API_KEY`

**API Specific**:
- `JWT_SECRET`, `SECRET_KEY`
- `MASTER_INTERNAL_API_KEY`

**Bots**:
- `BOTS_INTERNAL_API_KEY` (shared by all bots)
- `TELEGRAM_BOT_TOKEN_AFFILIATE`
- `TELEGRAM_BOT_TOKEN_ALIEXPRESS`
- `TELEGRAM_BOT_TOKEN_OFERTAS`
- `TELEGRAM_BOT_TOKEN_ALERTAS`

**Social Media**:
- `INSTAGRAM_ACCESS_TOKEN`
- `FACEBOOK_ACCESS_TOKEN`
- `TWITTER_API_KEY`, `TWITTER_API_SECRET`

### **Future: HashiCorp Vault**

Migration to HashiCorp Vault is planned for centralized, secure secret management with:
- Centralized secret storage
- Audit logs
- Secret rotation
- Fine-grained access control

---

## **Memory Bank Structure**

All project documentation lives in Memory Banks. **NEVER create standalone .md files.**

### **Decentralized Documentation Structure**

**⚠️ NEW PATTERN**: Documentation is now **decentralized** - each service has its own Memory Bank in its repository.

**Why Decentralized?**
- Git history preserves documentation with code
- Clear ownership: each team controls their docs
- Easy onboarding: clone repo = get code + docs
- Reduced confusion: docs near where they're used

### **Available Memory Banks**

```
ofertasdachina/docs/
├── memory-bank/                         # Central (cross-cutting concerns)
└── memory-bank-infrastructure/          # DevOps, Traefik, Secrets, Ports

ofertasdachina/repos/
├── ofertachina-api/docs/memory-bank/    # Backend API
├── ofertachina-bots/memory-bank-BOTS/   # Telegram Bots (overview)
├── ofertachina-bots/bots/{bot}/memory-bank-{bot}/  # Individual bots
├── ofertachina-social/memory-bank/      # Social Media Agent
└── impressao3dbr/docs/memory-bank/      # 3D printing marketplace
```

**For complete mapping, see:** `/home/admin/ofertasdachina/docs/memory-bank/PROJECT-STRUCTURE-MAP.md`

### **Standard Structure Per Memory Bank**

```
memory-bank-{service}/
├── 00-overview.md           # What? Why? Start here
├── 01-architecture.md       # Design, components, flows
├── 02-components.md         # Modules, classes, functions
├── 03-process.md            # Workflows, algorithms
├── 04-active-context.md     # Current state, decisions
├── 05-progress-log.md       # Complete history of changes
├── 06-deployment.md         # Deploy, rollback, troubleshooting
└── 07-reference.md          # Links, external resources
```

**When to update:**
- Architectural changes → `01-architecture.md`
- New features/components → `02-components.md`
- Current work → `04-active-context.md`
- After completing tasks → `05-progress-log.md`

See: `.github/instructions/memory-bank.instructions.md` for workflows.

---

## **Communication Patterns**

### **Bot ↔ API Communication**

```
Telegram User → Telegram API → Webhook (Traefik) → Bot (Flask) → API (REST) → Database
```

**Authentication:**
- Bots use `BOTS_INTERNAL_API_KEY` (shared)
- API validates via middleware
- JWT tokens for user sessions

### **Data Flow**

```
URL Input → Site Detection → Scraper → Data Extraction → AI Enrichment (Gemini) → Cache → Distribution (Bot/Social/Web)
```

---

## **Telegram Bot Architecture**

### **ModularBot Template**

All bots inherit from `ModularBot` base class:
- **BotBase Foundation:** Core Telegram API + database + config
- **WSGI Pattern:** Flask app with Gunicorn workers
- **Handler System:** Automatic command handler registration
- **Shared Components:** `bots/shared/` (services, templates, core)

### **Webhook Flow**

```nginx
# Traefik routing
webhook.ofertachina.cloud/bot/<TOKEN> → Container Port

affiliate_helper_bot:    8002 → /bot/TOKEN_AFFILIATE
aliexpress_bot:          8004 → /bot/TOKEN_ALIEXPRESS
ofertas_bot:             8005 → /bot/TOKEN_OFERTAS
alertas_bot:             8006 → /bot/TOKEN_ALERTAS
```

### **Bot-Specific Features**

**affiliate_helper_bot:**
- Enrich product links with affiliate tracking
- Generate AI-powered product descriptions via Gemini
- Fallback to manual processing if API unavailable

**aliexpress_bot:**
- Search AliExpress products
- Extract product details
- Generate shareable offers

**ofertas_bot:**
- Ingest deals from multiple sources
- Format and validate product information
- Queue for distribution

**alertas_bot:**
- Broadcast offers to subscribers
- Manage user preferences
- Track engagement metrics

---

## **Development Workflow**

### **Local Development**

1. **Clone repository:**
   ```bash
   cd /home/admin/ofertasdachina/repos/{service}/
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Load secrets:**
   ```bash
   export INFISICAL_SERVICE_TOKEN="st.xxxxx..."
   python3 scripts/setup/secrets_manager.py get-all /service
   ```

4. **Run service:**
   ```bash
   python main.py
   ```

### **Docker Development**

```bash
# Build service
docker-compose build {service}

# Run service
docker-compose up -d {service}

# View logs
docker logs -f {service-container}

# Restart service
docker-compose restart {service}
```

### **Testing**

```bash
# Run unit tests
pytest tests/

# Run specific test
pytest tests/test_module.py::test_function

# Run with coverage
pytest --cov=src tests/
```

---

## **Database Schema**

### **MariaDB**

**Host:** `mariadb-ofertachina:3306`  
**Database:** `ofertachina_db`  
**User:** `ofertachina_user`

**Key Tables:**
- `users` - User accounts and profiles
- `offers` - Product offers and deals
- `affiliates` - Affiliate link tracking
- `subscriptions` - User notification preferences
- `sessions` - User sessions

### **Redis**

**Host:** `redis-ofertachina:6379`

**Databases:**
- DB 0: Offer cache
- DB 1: User sessions
- DB 2: Rate limiting

---

## **External Integrations**

### **Telegram Bot API**
- Webhook-based updates (not polling)
- HTTPS required (via Nginx reverse proxy)
- Rate limits: 30 req/sec per bot

### **Google Gemini API**
- Model: `gemini-1.5-flash`
- Used for: Product descriptions, content generation
- Rate limits: Varies by API key tier

### **Social Media APIs**
- Instagram Graph API
- Facebook Graph API
- Twitter API v2
- LinkedIn API

---

## **Monitoring & Health Checks**

Each service should expose `/health` endpoint:

```json
{
  "status": "healthy",
  "uptime": 12345,
  "timestamp": "2025-11-11T10:30:00Z",
  "dependencies": {
    "database": "ok",
    "cache": "ok",
    "messagequeue": "ok"
  }
}
```

**Check service health:**
```bash
curl http://localhost:8080/health
```

---

## **Common Patterns**

### **Error Handling**
- Always use try-except blocks for external calls
- Log errors with context (user_id, action, timestamp)
- Return user-friendly error messages
- Implement retry logic with exponential backoff

### **Configuration Management**
- Load from environment variables
- Use `.env.example` for documentation
- Never commit secrets to git
- Validate required config at startup

### **Database Access**
- Use connection pooling
- Implement proper transaction handling
- Add indexes for common queries
- Use prepared statements (prevent SQL injection)

### **API Design**
- RESTful endpoints
- Consistent error responses
- Pagination for list endpoints
- Rate limiting on public endpoints

---

## **Troubleshooting**

### **Service Not Responding**
1. Check logs: `docker logs <container>`
2. Check health: `curl http://localhost:<port>/health`
3. Verify network: `docker network inspect ofertachina-network`
4. Check secrets: `python3 scripts/setup/secrets_manager.py audit`

### **Database Connection Issues**
1. Verify MariaDB is running: `docker ps | grep mariadb`
2. Test connection: `docker exec -it mariadb-ofertachina mysql -u root -p`
3. Check credentials in Infisical

### **Bot Webhook Issues**
1. Verify Nginx is running and routing correctly
2. Check webhook URL is set: `curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
3. Verify SSL certificate is valid
4. Check bot container logs

---

## **Key Files & Directories**

**Root:**
- `/home/admin/agents.md` - Complete agent architecture documentation
- `/home/admin/ofertasdachina/` - Main project directory

**Infrastructure:**
- `infra/docker-compose-networks.yml` - Network definitions
- `infra/nginx/` - Nginx configurations
- `infra/databases/` - Database init scripts

**Scripts:**
- `scripts/setup/secrets_manager.py` - Infisical secrets management
- `scripts/backup/` - Backup automation
- `scripts/deploy/` - Deployment scripts

**Documentation:**
- `docs/memory-bank*/` - All service documentation
- See `.github/instructions/no-unnecessary-files.instructions.md` for documentation rules

---

## **Testing Strategy - Hybrid Approach**

### **Core Decision: venv for Unit + Docker for Integration**

**TASK113-115 Testing Phase** uses a hybrid testing approach:

```
Unit Tests (venv)           → Fast feedback <2s
    ↓
Integration Tests (Docker) → Production-like environment
    ↓
CI/CD Tests (GitHub Actions) → Automated validation
```

### **Unit Tests** (venv)
- Run in local Python environment
- Test services, repositories, models in isolation
- Use mocks for external dependencies (Redis, Gemini, etc)
- ~98 tests, <2s execution
- **Files**: `tests/unit/test_*.py`

### **Integration Tests** (Docker)
- Run with real MySQL, Redis, external APIs
- Test all 24 endpoints with database
- Validate caching, concurrent requests, auth
- ~50 tests, <30s execution
- **Files**: `tests/integration/test_*.py`
- **Prerequisites**: `docker-compose -f docker-compose.test.yml up -d`

### **Test Configuration**
- **Framework**: pytest + pytest-asyncio + pytest-cov
- **Config**: `pytest.ini` + `tests/conftest.py`
- **Fixtures**: Shared in `conftest.py`, per-type in `unit/conftest.py` and `integration/conftest.py`
- **Markers**: `@pytest.mark.asyncio`, `@pytest.mark.unit`, `@pytest.mark.integration`

### **Running Tests Locally**

```bash
# Quick feedback (unit tests only)
pytest tests/unit/ -v --tb=short

# Full validation (unit + integration)
docker-compose -f docker-compose.test.yml up -d
pytest tests/unit/ tests/integration/ -v
docker-compose -f docker-compose.test.yml down

# With coverage report
pytest --cov=fastapi_app --cov-report=html
open htmlcov/index.html
```

### **Coverage Targets**
- Services: >80%
- Repositories: >80%
- Routers: >75%
- Overall: >80%

### **Full Documentation**
See: `docs/memory-bank-api/04-testing-strategy.md`

---

**For complete agent details, refer to:** `/home/admin/agents.md`  
**For project structure and Memory Bank locations, refer to:** `/home/admin/ofertasdachina/docs/memory-bank/PROJECT-STRUCTURE-MAP.md`  
**For Memory Bank workflows, refer to:** `.github/instructions/memory-bank.instructions.md`  
**For documentation rules, refer to:** `.github/instructions/no-unnecessary-files.instructions.md`

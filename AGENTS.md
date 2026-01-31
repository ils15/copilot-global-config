# VSCode Copilot Agents - Central Orchestrator

## 🏛️ Agent Architecture

Arquitetura baseada em **padrão Conductor-Delegate** com 9 deidades mitológicas:
- 1 Orchestrator (Zeus) + 8 Specialized Subagents

### Orchestrator Tier

#### ⚡ **Zeus** (.github/agents/zeus.agent.md)
Central coordinator delegating work to specialized subagents.

**When to use:** Complex feature implementation, multi-layer coordination, cross-functional tasks  
**Role:** Feature orchestration, phase transition, context management  
**Delegates to:** metis → apollo → {hermes, athena, tethys} → hephaestus → tyr → mnemosyne

**Example:**
```
/implement-feature Add JWT authentication to API

Zeus orchestrates:
1. Metis plans architecture
2. Apollo explores codebase
3. Hermes implements backend
4. Athena implements frontend
5. Tethys handles database migrations
6. Hephaestus updates Docker
7. Tyr reviews all changes
8. Mnemosyne documents
```

---

### Planning Tier

#### 🧠 **Metis** (.github/agents/metis-subagent.agent.md)
Strategic planner with research capability. Generates detailed TDD-driven implementation roadmaps.

**When to use:** Architecture decisions, technology research, detailed planning before implementation  
**Tools:** search, usages, fetch_webpage (for external research)  
**Calls:** apollo (for parallel discovery)  
**Skills:** plan-architecture.prompt  

**Example:**
```
/plan-architecture Implement caching layer (L1 local + L2 Redis)

Metis:
1. Researches caching patterns
2. Calls Apollo for existing cache references
3. Creates detailed TDD plan
4. Proposes implementation phases
5. Hands off to Zeus for execution
```

---

### Discovery Tier

#### 🔍 **Apollo** (.github/agents/apollo-subagent.agent.md)
Parallel file discovery and intelligence gathering. Can run 3-10 simultaneous searches.

**When to use:** Rapid codebase exploration, bug root cause discovery, cross-file pattern analysis  
**Tools:** search, usages (read-only parallel searches)  
**Parallelism:** Up to 10 simultaneous search queries  
**Skills:** debug-issue.prompt  

**Example:**
```
/debug-issue NullPointerException in user service

Apollo searches (parallel):
1. "UserService" class definition
2. "NullPointer" error messages
3. User initialization code
4. Recent git commits to UserService
5. Unit tests for UserService
6. Mock data in tests

→ Synthesizes findings into root cause
```

---

### Implementation Tier (Parallel Executors)

#### 🔥 **Hermes** (.github/agents/hermes-subagent.agent.md)
Backend APIs, FastAPI services, async business logic.

**When to use:** API endpoint implementation, service layer creation, async I/O handling  
**Specialization:** FastAPI, Python, async/await, TDD backend  
**Depends on:** tethys (database), hephaestus (deployment)  
**Skills:** backend-standards.instructions, tdd-testing, api-design, security-audit  
**Tools:** search, usages, read-file, edit, runCommands  

**Backend Standards Applied:**
- Async/await on ALL I/O operations
- Type hints on all parameters
- Max 300 lines per file
- TDD first (RED → GREEN → REFACTOR)
- >80% test coverage
- Error propagation (no silent fallbacks)

---

#### 💎 **Athena** (.github/agents/athena-subagent.agent.md)
Frontend UI/UX, React components, responsive design.

**When to use:** Component creation, UI improvements, accessibility fixes, state management  
**Specialization:** React, TypeScript, responsive design, WCAG accessibility  
**Depends on:** hermes (API endpoints)  
**Skills:** frontend-standards.instructions, tdd-testing, api-design  
**Tools:** search, usages, read-file, edit, runCommands  

**Frontend Standards Applied:**
- TypeScript strict mode
- Accessibility: ARIA, semantic HTML
- Responsive design (mobile-first)
- Component composition patterns
- State management discipline
- >80% test coverage (vitest)

---

#### 🌊 **Tethys** (.github/agents/tethys-subagent.agent.md)
Database design, SQL optimization, migration management.

**When to use:** Schema design, query optimization, N+1 prevention, migration strategy  
**Specialization:** SQLAlchemy ORM, Alembic migrations, query analysis  
**Dependencies:** metis (planning), hermes (schema needs)  
**Skills:** database-standards.instructions, database-migration, performance-optimization, security-audit  
**Tools:** search, usages, read-file, edit, runCommands  

**Database Standards Applied:**
- Zero-downtime migration strategy
- Backward compatibility (expand-contract)
- Index strategy for performance
- N+1 query prevention
- Query plan analysis (EXPLAIN ANALYZE)
- Connection pooling configuration

---

#### ⚙️ **Hephaestus** (.github/agents/hephaestus-subagent.agent.md)
Infrastructure, Docker containerization, deployment orchestration.

**When to use:** Container optimization, deployment strategy, infrastructure as code, CI/CD  
**Specialization:** Docker, docker-compose, multi-stage builds, health checks, CI/CD workflows  
**Depends on:** All agents (needs their deployment requirements)  
**Skills:** docker-deployment, performance-optimization  
**Tools:** search, usages, read-file, edit, runCommands  

**Infrastructure Standards Applied:**
- Multi-stage Docker builds
- Non-root user execution
- Health checks on all services
- Zero-downtime deployment strategy
- Environment variable management
- Secrets from vault (not hardcoded)

---

### Quality Assurance Tier

#### ⚖️ **Tyr** (.github/agents/tyr-subagent.agent.md)
Code review, security audit, quality gates.

**When to use:** Code review before merge, security scan, test coverage validation, architecture review  
**Specialization:** Code review checklist, OWASP security audit, >80% coverage validation  
**Reviews:** All outputs from hermes, athena, tethys  
**Skills:** code-review-standards.instructions, security-audit, tdd-testing  
**Tools:** search, usages, read-file, edit, runTasks  

**Quality Gates:**
- ✅ >80% test coverage
- ✅ All OWASP Top 10 checks pass
- ✅ No hardcoded secrets
- ✅ TypeScript strict mode (frontend)
- ✅ Type hints on all functions (backend)
- ✅ Accessibility compliance (frontend)
- ✅ No SQL injection vulnerabilities
- ✅ Proper error handling

---

### Memory Tier

#### 📚 **Mnemosyne** (.github/agents/mnemosyne-subagent.agent.md)
Memory bank management, decision documentation, progress tracking.

**When to use:** End of sprint/feature, decision documentation, retrospectives, memory updates  
**Specialization:** Knowledge preservation, institutional memory, task tracking  
**Maintains:** `/docs/memory-bank/` directory structure  
**Input from:** All agents feed information  
**Skills:** None specific (documentation focused)  

**Responsibilities:**
- [ ] Update memory bank with decisions
- [ ] Document architectural patterns discovered
- [ ] Track completed features in progress log
- [ ] Archive session decisions in notes
- [ ] Maintain task index and status

---

## 📋 Task Dispatch Patterns

### Pattern 1: Simple Bug Fix (Apollo → Hermes → Tyr)
```
User: /debug-issue API returns 500 on POST /users

1. Apollo runs 3-5 parallel searches
   ├─ Extract error stack trace
   ├─ Find POST /users endpoint
   ├─ Find UserService.create()
   └─ Check error handling

2. Hermes implements fix
   ├─ Add validation
   ├─ Add error handling
   └─ Write RED test first

3. Tyr reviews
   └─ Approve if coverage >80% + no OWASP issues
```

### Pattern 2: Feature Implementation (Metis → Hermes/Athena/Tethys → Tyr → Hephaestus)
```
User: /implement-feature Add email verification flow

1. Metis plans (triggers via /plan-architecture if needed)
   ├─ Design database schema
   ├─ Design API endpoints
   ├─ Design frontend components
   └─ Create TDD roadmap

2. Parallel implementation
   ├─ Hermes: POST /verify-email, POST /resend-code
   ├─ Athena: VerificationForm, CodeInput components
   └─ Tethys: VerificationCode & UserVerification tables

3. Tyr reviews all changes
   └─ Validates coverage, security, architecture

4. Hephaestus updates deployment
   └─ Docker changes, env variables, health checks
```

### Pattern 3: Performance Optimization (Apollo → Tethys → Tyr)
```
User: /optimize-database GET /products endpoint slow

1. Apollo discovers
   ├─ Current ProductService.list() implementation
   ├─ Current database queries
   └─ Related indexes

2. Tethys analyzes
   ├─ Runs EXPLAIN ANALYZE
   ├─ Identifies N+1 queries
   ├─ Proposes index strategy
   └─ Creates migration with TDD

3. Tyr validates
   └─ Benchmarks before/after
```

---

## 🔧 Direct Invocation

Each agent can be invoked directly for bypass orchestration:

```bash
# Invoke specific agent
@hermes: Create POST /products endpoint with TDD

@tethys: Optimize users table queries

@athena: Build ProductCard component with Storybook

@apollo: Find all uses of deprecated api.getUsers() method

@metis: Plan migration from REST to GraphQL

@tyr: Review this PR for security issues

@hephaestus: Create multi-stage Docker build for new service

@mnemosyne: Update memory bank with completed features

@zeus: Orchestrate full feature implementation
```

---

## 🎯 Agent Selection Guide

| Need | Agent | Trigger |
|------|-------|---------|
| Plan architecture | metis | `/plan-architecture` |
| Debug issue | apollo | `/debug-issue` |
| New API endpoint | hermes | Direct: @hermes |
| New component | athena | Direct: @athena |
| Database optimization | tethys | `/optimize-database` |
| Deploy changes | hephaestus | Direct: @hephaestus |
| Code review | tyr | `/review-code` |
| Document decisions | mnemosyne | Direct: @mnemosyne |
| Coordinate feature | zeus | `/implement-feature` |

---

## 📚 References

- **Agent Skills:** `.github/skills/*/SKILL.md`
- **Custom Instructions:** `.github/instructions/*-standards.instructions.md`
- **Prompt Files:** `.github/prompts/*.prompt.md`
- **Agent Definitions:** `.github/agents/*.agent.md`
- **Memory Bank:** `/docs/memory-bank/`
- **VSCode Settings:** `.vscode/settings.json`

---

**Last Updated:** [AUTO-UPDATED on agent creation]  
**Total Agents:** 9 (1 orchestrator + 8 specialized)  
**Total Skills:** 6  
**Total Custom Instructions:** 5  
**Total Prompt Files:** 5  
**Architecture Pattern:** Conductor-Delegate  
**Mythology Reference:** Greek, Norse, Egyptian Deities

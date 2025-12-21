---
description: |
  GitHub Copilot custom instructions for Ofertasdachina platform.
  This file centralizes all custom instruction rules, agent routing,
  and architectural guidelines for the project.
version: "1.0"
---

# 🤖 GitHub Copilot - Custom Instructions
**Ofertasdachina Platform**

---

## 📖 Quick Navigation

### **Execution & Development**
- [Copilot Execution Guidelines](/.github/instructions/copilot-execution.md) - Code quality, review, best practices
- [Core Rules](/.github/instructions/core.rules.md) - Planning, documentation, task management rules
- [Code Simplification](/.github/instructions/code-simplification.md) - Complexity reduction, anti-patterns

### **Architecture & Planning**
- [Memory Bank Guidelines](/.github/instructions/memory-bank-guidelines.md) - How to use Memory Bank
- [Agents Analysis](/.github/instructions/agents-analysis.md) - Agent roles and responsibilities
- [Agent Routing & Handoffs](/.github/instructions/subagents.md) - When to use each agent

### **Audits & Quality**
- [Bot Audit System](/.github/instructions/bot-audit.md) - 25-question quarterly bot audits
- [API Audit](/.github/instructions/api-audit.md) - API quality and performance audits
- [Impressão 3D Audit](/.github/instructions/impressao3d-audit.md) - E-commerce platform audits
- [Social Post Audit](/.github/instructions/socialpost-audit.md) - Social media posting audits

### **Design & UX**
- [Telegram Bot UI Design](/.github/instructions/telegram-bot-ui.md) - Bot keyboard, buttons, UX patterns
- [Web UI/UX Analysis](/.github/instructions/web-ui-ux.md) - Typography, colors, layout, accessibility

### **Feature-Specific**
- [Impressão 3D Versioning](/.github/instructions/impressao3d-versioning.md) - Version control strategies
- [Memory Bank Structure](/.github/instructions/memory-bank-structure.md) - File organization guidelines

---

## 🎯 Core Directives

### **1. Planning (MANDATORY)**
✅ Always create **INTERNAL IMPLEMENTATION PLAN** before coding
```
📜 INTERNAL IMPLEMENTATION PLAN
🎯 GOAL: [Single sentence objective]
🔬 SCOPE: [Files and functions to modify]
⚖️ JUSTIFICATION: [Brief reason]
⚠️ RISKS: [Potential issues or "None"]
🛠️ STEPS: [Numbered action items]
```

### **2. Code Quality**
✅ **Simplicity First** - Readable code > clever code  
✅ **DRY Principle** - No duplication  
✅ **SOLID Principles** - Single responsibility, proper abstraction  
✅ **500-Line Limit** - Refactor files exceeding 500 lines  
✅ **No God Objects** - Functions do one thing well  

### **3. Documentation**
✅ **Memory Bank Only** - All docs go in `/docs/memory-bank/`  
✅ **NO Auto-Generated Files** - Never create .md files automatically  
✅ **Inline Comments** - Why, not what  
✅ **Docstrings** - Every function has clear docstrings  

### **4. Self-Review (MANDATORY)**
After changes:
1. ✅ Read ALL modified code
2. ✅ Verify logic and edge cases
3. ✅ Check imports and dependencies
4. ✅ Validate inline documentation

---

## 🤖 Agent Selection Matrix

### **Quick Selection**
| Task Type | Agent | Keywords |
|-----------|-------|----------|
| **API Endpoints** | @Backend | `endpoint`, `router`, `FastAPI`, `async` |
| **React Components** | @Frontend | `component`, `page`, `React`, `TypeScript` |
| **Database Changes** | @Database | `migration`, `schema`, `Alembic` |
| **Docker/Container** | @Docker | `Dockerfile`, `docker-compose`, `build`, `image` |
| **Infrastructure** | @Infra | `nginx`, `Traefik`, `deployment`, `SSL` |
| **Linux/Bash** | @Linux | `bash`, `shell`, `script`, `chmod`, `apt` |
| **Git Operations** | @GitHub | `commit`, `push`, `PR`, `branch`, `merge` |
| **Bug Investigation** | @Debug | `bug`, `error`, `500`, `fix`, `issue` |
| **Code Review** | @Reviewer | `review`, `validate`, `check`, `verify` |
| **Planning** | @Planner | `plan`, `design`, `Memory Bank`, `TODO` |

**Full Agents List**: See [Agents Analysis](/.github/instructions/agents-analysis.md)

---

## 📚 Skills Framework (NEW - PHASE 1)

All agents reference reusable **skill modules** for consistency:

| Skill | Purpose | Used By |
|-------|---------|---------|
| **architecture-patterns** | System design, trade-offs, anti-patterns | architect, critic, analyst |
| **code-review-checklist** | Code quality standards, review process | reviewer, qa, backend, frontend, database |
| **engineering-standards** | SOLID, DRY, YAGNI, code organization | ALL agents |
| **memory-contract** | Memory Bank API, memory usage patterns | MANDATORY all agents |
| **release-procedures** | SemVer, changelog, deployment strategies | devops, github, docker, infra |
| **security-patterns** | CIA Triad, OWASP, STRIDE, secure coding | security, backend, frontend, database, reviewer |
| **testing-patterns** | Test pyramid, TDD, test coverage | qa, reviewer, backend, frontend, debug |

**How to Use**: When a task requires deep knowledge of a pattern, refer to the relevant skill module.

Example: "I need to review code for security issues → Check `security-patterns` skill"

---

## 🚨 Escalation Framework (NEW - PHASE 3)

All 26 agents now support structured escalation. Before escalating:

**IMMEDIATE (< 1 hour)**
- Critical blocker preventing work
- Security vulnerability found
- Plan has fundamental flaw
- Escalate to: **Roadmap** or **Critic**

**SAME-DAY (< 4 hours)**
- Technical unknowns requiring research
- Need architectural guidance
- Escalate to: **Analyst** or **Architect**

**PLAN-LEVEL (< 24 hours)**
- Plan is incomplete or outdated
- Requirements need clarification
- Escalate to: **Planner**

**PATTERN (3+ occurrences)**
- Same issue appears multiple times
- Process needs improvement
- Escalate to: **ProcessImprovement**

---

## 🔄 Two-Stage Release Workflow (NEW - PHASE 3)

Release process now separated into 2 stages:

**Stage 1: PRE-RELEASE VALIDATION (24h before)**
- @docker: Build images + security scan
- @infra: Deploy to staging + smoke tests
- @qa: Full test suite + performance baseline
- @reviewer: Final code review + changelog validation

**Stage 2: RELEASE EXECUTION (if Stage 1 ✅)**
- @github: Create release tag + notes
- @docker: Push images to registry
- @devops: Blue-Green or Canary deployment
- @infra: Monitor health + alert on issues

**Rollback**: If Stage 2 fails, immediate traffic shift back to previous version.

See [devops.agent.md](/.github/agents/devops.agent.md) for full workflow.

---

## 🔀 Handoff Chain Example (Full Feature)

```
@Planner (plan) 
  ↓
@Backend (API implementation) 
  ↓
@Frontend (UI components) 
  ↓
@Reviewer (code review + tests) 
  ↓
@Documentation (Memory Bank update)
  ✅ COMPLETE
```

---

## 📋 Development Standards

### **Code Organization**
```
backend/
  routers/          # API endpoints
  services/         # Business logic
  repositories/     # Data access
  models/          # SQLAlchemy models
  schemas/         # Pydantic schemas
  utils/           # Utilities
  
frontend/src/
  components/      # Reusable React components
  pages/          # Page-level components
  hooks/          # Custom React hooks
  lib/            # Utilities and helpers
  styles/         # CSS/styling
```

### **Naming Conventions**
- **Files**: `snake_case` (Python), `camelCase` (JavaScript)
- **Classes**: `PascalCase`
- **Functions**: `snake_case` or `camelCase`
- **Constants**: `UPPER_SNAKE_CASE`

### **Async/Await (Python)**
✅ Always use async for I/O operations  
✅ Use `asyncio`, `aiohttp`, SQLAlchemy async  
✅ Plan for timeouts and network failures

---

## 🔒 Security & Validation

### **Input Validation**
✅ Validate ALL inputs  
✅ Sanitize data  
✅ Use strong typing  
✅ Enforce length limits  

### **Secrets Management**
- Store secrets in environment variables or Vault
- NEVER commit secrets to Git
- Use `.env.example` (no real values)

### **Error Handling**
✅ Comprehensive error coverage  
✅ Graceful degradation  
✅ User-friendly messages  
✅ Sufficient logging context

---

## 🤐 Output Rules (MANDATORY - Anti-Verbosity)

### RULE A: Never Use `cat` in Responses
❌ **NEVER**: `cat file.txt` or paste full file content  
✅ **INSTEAD**: Use `file:line-range` reference format

### RULE B: Concise Reporting Only
❌ **NEVER**: 20-line status report with full paths  
✅ **INSTEAD**: Bullet points max 5 items, 1 line each

### RULE C: No Output Dumps
❌ **NEVER**: Paste JSON/logs/test output  
✅ **INSTEAD**: `Test results: 24/24 passing ✅`

### RULE D: Use Reference Format Always
✅ **ONLY**: `backend/services/auth.py:45-78 (JWT validation)`  
❌ **NEVER**: Paste 50 lines of actual code

### RULE E: Clean Summary Template
Every response ends with:
```
📊 SUMMARY
- ✅ [What was done]
- 📝 [Files modified: count]
- 🔗 [Next: agent or action]
```

**VIOLATIONS TO AVOID**: Long explanations, code dumps, debug output, introductions

---

## 📊 Quality Checklist (Before Completion)

- [ ] Code follows all core rules
- [ ] All modified code has been self-reviewed
- [ ] Docstrings/comments are clear
- [ ] No linting errors (flake8, ESLint)
- [ ] Type checking passes (mypy, tsc)
- [ ] Build succeeds
- [ ] Memory Bank updated (if complex task)
- [ ] No unnecessary .md files created
- [ ] Edge cases considered
- [ ] Output Rules followed (RULE A-E)

---

## 🚀 Related Documentation

- **Project Repository**: [Ofertasdachina](https://github.com/ofertasdachina/ofertasdachina)
- **Memory Bank**: `/docs/memory-bank/` - Project context, progress, task tracking
- **Agent Instructions**: `/.github/instructions/` - Detailed agent guidelines
- **Configuration**: See individual `.env.example` files

---

## 📝 Version History

- **v1.0** (2025-12-19): Initial custom instructions setup with GitHub-compliant structure

# VSCode Copilot Agents - Central Orchestrator

## 🏛️ Agent Architecture

Architecture based on **Conductor-Delegate pattern** with 9 mythological deities:
- 1 Orchestrator (Zeus) + 8 Specialized Subagents

### Orchestrator Tier

#### ⚡ **Zeus** (agents/zeus.agent.md)
Central coordinator delegating work to specialized subagents.

**When to use:** Complex feature implementation, multi-layer coordination, cross-functional tasks  
**Role:** Feature orchestration, phase transition, context management  
**Delegates to:** athena → apollo → {hermes, aphrodite, maat} → ra → temis → mnemosyne

**Example:**
```
/implement-feature Add JWT authentication to API

Zeus orchestrates:
1. Athena plans architecture
2. Apollo explores codebase
3. Hermes implements backend
4. Athena implements frontend
5. Maat handles database migrations
6. Ra updates Docker
7. Temis reviews all changes
8. Mnemosyne documents
```

---

### Planning Tier

#### 🧠 **Athena** (agents/athena.agent.md)
Strategic planner with research capability. Generates detailed TDD-driven implementation roadmaps.

**When to use:** Architecture decisions, technology research, detailed planning before implementation  
**Tools:** search, usages, fetch_webpage (for external research)  
**Calls:** apollo (for codebase discovery), hermes (for implementation)  
**Skills:** plan-architecture.prompt  

**Example:**
```
/plan-architecture Implement caching layer (L1 local + L2 Redis)

Athena:
1. Researches caching patterns
2. Calls Hermes for backend implementation
3. Creates detailed TDD plan
4. Proposes implementation phases
5. Hands off to Zeus for execution
```

---

### Discovery Tier

#### 🔍 **Apollo** (agents/apollo.agent.md)
Basic code search and discovery agent. Supports planner, debugger, and other agents with rapid file location and pattern finding.

**When to use:** Rapid codebase exploration, bug root cause discovery, finding files before implementation, helping any agent locate code  
**Called by:** Athena (planning), Zeus (debugging), Hermes/Aphrodite/Maat (locating existing patterns)  
**Tools:** search, usages (read-only parallel searches)  
**Parallelism:** Up to 10 simultaneous search queries  
**Web Research:** Suggests official docs, RFCs, and best practices for Athena to fetch  
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
→ Recommends Athena fetch: SQLAlchemy async patterns, FastAPI error handling best practices
```

---

### Implementation Tier (Parallel Executors)

#### 🔥 **Hermes** (agents/hermes.agent.md)
Backend APIs, FastAPI services, async business logic.

**When to use:** API endpoint implementation, service layer creation, async I/O handling  
**Specialization:** FastAPI, Python, async/await, TDD backend  
**Depends on:** maat (database), ra (deployment)  
**Can call:** apollo (for codebase discovery)  
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

#### 💎 **Aphrodite** (agents/aphrodite.agent.md)
Frontend UI/UX, React components, responsive design.

**When to use:** Component creation, UI improvements, accessibility fixes, state management  
**Specialization:** React, TypeScript, responsive design, WCAG accessibility  
**Depends on:** hermes (API endpoints)  
**Can call:** apollo (for component discovery)  
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

#### 🌊 **Maat** (agents/maat.agent.md)
Database design, SQL optimization, migration management.

**When to use:** Schema design, query optimization, N+1 prevention, migration strategy  
**Specialization:** SQLAlchemy ORM, Alembic migrations, query analysis  
**Dependencies:** athena (planning), hermes (schema needs)  
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

#### ⚙️ **Ra** (agents/ra.agent.md)
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

#### ⚖️ **Temis** (agents/temis.agent.md)
Code review, security audit, quality gates.

**When to use:** Code review before merge, security scan, test coverage validation, architecture review  
**Specialization:** Code review checklist, OWASP security audit, >80% coverage validation  
**Reviews:** All outputs from hermes, aphrodite, maat  
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

#### 📚 **Mnemosyne** (agents/mnemosyne.agent.md)
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

---

## ✋ MANDATORY PAUSE POINTS

The Zeus system is controlled by the user through **MANDATORY PAUSE POINTS** at each phase:

### Pause Point 1: Planning Approval
```
Athena creates detailed plan
     ↓
⏸️  STOP: User reviews and approves plan
     ↓
Plan saved in: plans/<feature-name>/plan.md
```

### Pause Point 2: Phase Implementation Review
```
Hermes/Aphrodite/Maat implements phase
     ↓
Temis reviews code
     ↓
⏸️  STOP: Show result and ask for confirmation
     ↓
Result saved in: plans/<feature-name>/phase-N-complete.md
```

### Pause Point 3: Git Commit
```
Zeus generates commit message
     ↓
⏸️  STOP: User executes "git commit" manually
     ↓
Next phase starts
```

**Benefit:** You maintain control and can interrupt at any time.

---

## 📋 Task Dispatch Patterns

### Pattern 1: Simple Bug Fix (Apollo → Hermes → Temis)
```
User: /debug-issue API returns 500 on POST /users

1. Apollo runs 3-5 parallel searches
   ├─ Extract error stack trace
   ├─ Find POST /users endpoint
   ├─ Find UserService.create()
   └─ Check error handling

2. Hermes implements fix (TDD WORKFLOW)
   ├─ Write FAILING test first
   ├─ Run test → expects FAILURE/RED
   ├─ Write minimal code to fix
   ├─ Run test → expects PASS/GREEN
   └─ Refactor and document

3. Temis reviews
   └─ Approve if coverage >80% + no OWASP issues
   
⏸️  MANDATORY STOP: User commits to git
```

### Pattern 2: Feature Implementation (Athena → Hermes/Aphrodite/Maat → Temis → Ra)
```
User: /implement-feature Add email verification flow

1. Athena plans (triggers via /plan-architecture if needed)
   ├─ Design database schema
   ├─ Design API endpoints
   ├─ Design frontend components
   └─ Create TDD roadmap with 3-10 phases
   
⏸️  MANDATORY STOP: User approves plan
   └─ Saved: plans/email-verification/plan.md

2. For each phase (Parallel execution allowed):
   
   Phase N Implementation:
   ├─ Hermes: Write FAILING tests → minimal code → PASSING tests
   ├─ Aphrodite: Write FAILING tests → minimal code → PASSING tests  
   └─ Maat: Write migration tests → minimal schema → passing tests
   
   Phase N Review:
   ├─ Temis validates >80% coverage + OWASP compliance
   └─ Saved: plans/email-verification/phase-N-complete.md
   
⏸️  MANDATORY STOP: User commits phase (git commit)

3. After all phases:

4. Ra updates deployment
   └─ Docker changes, env variables, health checks
   └─ Final artifact: plans/email-verification/complete.md
```

### Pattern 3: Performance Optimization (Apollo → Maat → Temis)
```
User: /optimize-database GET /products endpoint slow

1. Apollo discovers (PARALLEL SEARCHES: 3-10)
   ├─ Current ProductService.list() implementation
   ├─ Current database queries  
   ├─ Related indexes
   ├─ N+1 patterns
   └─ Cache usage
   
   ⏸️  Apollo returns structured findings, not raw code

2. Maat analyzes (CONTEXT EFFICIENT)
   ├─ Runs EXPLAIN ANALYZE
   ├─ Identifies N+1 queries
   ├─ Proposes index strategy
   ├─ Writes migration test FIRST (TDD)
   └─ Implements minimal migration code

3. Temis validates
   ├─ Benchmarks before/after
   ├─ Validates >80% test coverage
   └─ Final artifact: plans/optimize-products/complete.md
   
⏸️  MANDATORY STOP: User commits to git
```

---

## 🧠 CONTEXT WINDOW MANAGEMENT

Each specialized agent **conserves tokens** through strategies:

### Apollo (Discovery)
- **Input:** Problem description
- **Output:** Structured SUMMARY, NOT raw code
- **Strategy:** Parallel search (3-10 simultaneous) returns only high-signal findings
- **Savings:** 60-70% fewer tokens than raw code dump

### Hermes/Aphrodite/Maat (Implementation)
- **Input:** Specific phase scope + tests to pass
- **Output:** ONLY files it modifies in this phase
- **Strategy:** Doesn't re-read complete architecture, only its files
- **Savings:** 50% fewer tokens vs monolithic agent

### Temis (Review)
- **Input:** Git diff (changed files only)
- **Output:** Structured comments with status (APPROVED/NEEDS_REVISION/FAILED)
- **Strategy:** Reviews only changed lines, not entire repository
- **Savings:** 60% fewer tokens than full codebase review

### Result
- **Traditional:** Single agent uses 80-90% context only on research/analysis
- **Zeus system:** 10-15% context for analysis, **70-80% free** for deep reasoning

---

## 🎯 TDD ENFORCEMENT WORKFLOW

All implementation agents (Hermes, Aphrodite, Maat) follow **RIGOROUSLY**:

### Phase 1: RED (Test Fails)
```python
# Write test FIRST
def test_user_password_hashing():
    user = User(email="test@example.com", password="secret123")
    assert user.password != "secret123"  # Should be hashed
    assert user.verify_password("secret123")  # Verify works

# Run test → FAILS/RED ❌
FAILED: AssertionError: password should be hashed
```

### Phase 2: GREEN (Test Passes)
```python
# Write MINIMAL code to make test pass
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = hash_password(password)  # Minimal: just hash
    
    def verify_password(self, plaintext):
        return verify_hash(plaintext, self.password)

# Run test → PASSES/GREEN ✅
PASSED: user password is hashed and verified
```

### Phase 3: REFACTOR
```python
# Improve code quality WITHOUT changing behavior
# Add validation, documentation, optimization
class User:
    """User model with secure password handling."""
    
    def __init__(self, email: str, password: str):
        if not email or not password:
            raise ValueError("Email and password required")
        self.email = email
        self.password = self._hash_password(password)
    
    @staticmethod
    def _hash_password(plaintext: str) -> str:
        """Hash password using bcrypt."""
        return bcrypt.hashpw(plaintext.encode(), bcrypt.gensalt())
    
    def verify_password(self, plaintext: str) -> bool:
        """Verify plaintext password against hash."""
        return bcrypt.checkpw(plaintext.encode(), self.password)

# Run test → STILL PASSES ✅
```

### TDD Checklist
- [ ] Write FAILING test first
- [ ] Run test, see RED/FAILED
- [ ] Write minimal code to pass
- [ ] Run test, see GREEN/PASSED
- [ ] Refactor if needed
- [ ] All tests still pass
- [ ] Coverage >80%

---

## 📁 PLAN DIRECTORY STRUCTURE

Each feature creates a documented directory:

```
plans/
├── .gitignore          # Ignore plans by default
├── README.md          # How to use plan directory
│
└── <feature-name>/
    ├── plan.md        # Plan approved by user
    ├── phase-1-complete.md
    ├── phase-2-complete.md
    ├── phase-3-complete.md
    └── complete.md    # Final summary
```

### plan.md (Created by Athena, Approved by User)
```markdown
# Feature: Email Verification Flow

**Status:** APPROVED by user on Feb 5, 2026

## Overview
Add email verification to new user registrations.

## Phases (3 total)

### Phase 1: Database Schema
- Create VerificationCode table with TTL
- Add verified_at field to User
- Tests first: validation, TTL expiry

### Phase 2: Email Service
- Create EmailService for sending
- Create VerifyEmail handler
- Tests: happy path, error handling

### Phase 3: Frontend Integration
- Create VerificationForm component
- Create ResendEmail button
- Tests: form submission, error display

## Files Affected
- Backend: models/User, models/VerificationCode, services/email.py
- Frontend: components/VerificationForm.tsx, hooks/useVerification.ts
```

### phase-N-complete.md (Created after each phase passes Temis review)
```markdown
# Phase 1 Complete: Database Schema

**Status:** APPROVED by Temis on Feb 5, 2026
**Coverage:** 94% (exceeds 80% requirement)

## Changes
- ✅ Created models/VerificationCode.py
- ✅ Modified models/User.py (added verified_at field)
- ✅ Created migrations/002_add_verification.py

## Tests Added
- test_verification_code_creation
- test_verification_code_expiry
- test_user_verified_at_field

## Git Commit
```
feat: Add email verification database schema

- Create VerificationCode model with 24h TTL
- Add verified_at timestamp to User
- Implement comprehensive tests (94% coverage)
```

## Decisions Made
- Used UUID for verification codes (not sequential integers)
- TTL enforced by trigger, not application logic
```

### complete.md (Final summary after all phases)
```markdown
# Feature Complete: Email Verification Flow

**Total Phases Completed:** 3  
**Total Coverage:** 92%  
**Total Files Modified:** 7  
**Total Time:** ~2 hours agent time  

## Phases
- ✅ Phase 1: Database Schema
- ✅ Phase 2: Email Service
- ✅ Phase 3: Frontend Integration

## Files Impacted
- models/User.py
- models/VerificationCode.py
- services/EmailService.py
- components/VerificationForm.tsx
- hooks/useVerification.ts
- migrations/002_add_verification.py
- tests/test_verification.py

## Next Steps
- [ ] Deploy to staging
- [ ] QA testing with real emails
- [ ] Deploy to production
```

---

## 🔧 Direct Invocation

Each agent can be invoked directly for bypass orchestration:

```bash
# Invoke specific agent
@apollo: Find all authentication-related files

@athena: Plan email verification feature

@hermes: Create POST /products endpoint with TDD

@aphrodite: Build ProductCard component with Storybook

@maat: Optimize users table queries

@ra: Create multi-stage Docker build for new service

@temis: Review this PR for security issues

@mnemosyne: Update memory bank with completed features

@zeus: Orchestrate full feature implementation
```

---

## 🎯 Agent Selection Guide

| Need | Agent | Trigger |
|------|-------|---------|
| Plan architecture | athena | `/plan-architecture` |
| Debug issue | apollo | `/debug-issue` |
| Find files/code | apollo | Direct: @apollo |
| New API endpoint | hermes | Direct: @hermes |
| New component | aphrodite | Direct: @aphrodite |
| Database optimization | maat | `/optimize-database` |
| Deploy changes | ra | Direct: @ra |
| Code review | temis | `/review-code` |
| Document decisions | mnemosyne | Direct: @mnemosyne |
| Coordinate feature | zeus | `/implement-feature` |

---

## 🎯 MODEL FALLBACK STRATEGY

Each agent supports multiple models with automatic fallback:

```yaml
# Zeus (Orchestrator)
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
# Prioritizes the most capable, fallback if unavailable

# Athena (Planning)
model: ['GPT-5 (copilot)', 'Claude Sonnet 4.5 (copilot)']
# GPT-5 better for reasoning in planning

# Apollo (Discovery)
model: ['Gemini 3 Flash (copilot)', 'Claude Haiku 4.5 (copilot)']
# Flash is fast for parallel searches

# Hermes/Aphrodite/Maat (Implementation)
model: ['Claude Sonnet 4.5 (copilot)', 'Claude Haiku 4.5 (copilot)']
# Sonnet for complexity, fallback to Haiku (economical)

# Temis (Review)
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
# Requires deep reasoning for code review

# Mnemosyne (Memory)
model: ['Claude Haiku 4.5 (copilot)']  
# Haiku is sufficient for documentation
```

**Benefit:** If main model is unavailable, system uses fallback automatically.

---

## 🔧 CUSTOM AGENT EXTENSION

To create a new specialized agent (example: Database-Expert):

### Step 1: Create Agent File
```bash
mkdir -p .github/agents
cat > agents/database-expert-subagent.agent.md << 'EOF'
---
name: database-expert
user-invokable: false  # Only for internal delegation
description: Specialized database architect and query optimizer
argument-hint: "Analyze and optimize database schema and queries"
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
tools: ['search', 'usages', 'edit', 'runCommands']
---

You are a DATABASE EXPERT SUBAGENT.

**Your specialty:** SQL optimization, schema design, perf tuning
**Your scope:** Database layer changes, migrations, index strategy

**Core workflow:**
1. Analyze current database structure
2. Identify bottlenecks with EXPLAIN ANALYZE
3. Propose schema or index optimizations
4. Write migration tests FIRST (TDD)
5. Implement minimal schema changes
6. Return structured findings

[Add your detailed instructions]
EOF
```

### Step 2: Register with Zeus
Edit `agents/zeus.agent.md` and add:
```markdown
**10. DatabaseExpert-subagent**: SQL and schema design specialist
- Use for query performance analysis
- Invoke for complex schema designs
- Always returns structured findings, never raw SQL dumps
```

### Step 3: Register with Athena (for planning phase)
Edit `agents/athena.agent.md` and add:
```markdown
**When researching database architecture, delegate to DatabaseExpert-subagent:**
- Goal: Analyze current schema and identify optimization opportunities
- Instructions: Use EXPLAIN ANALYZE, check indexes, find N+1 patterns
- Return: Structured findings with specific recommendations
```

### Step 4: Test Integration
```bash
# Invoke directly
@database-expert: Analyze the users table queries for N+1 problems

# Or through Zeus
@zeus: Use database-expert to optimize the product search queries
```

### Custom Agent Checklist
- [ ] Create `.agent.md` file with proper frontmatter
- [ ] Set `user-invokable: false` if internal only
- [ ] Define tools needed (search, edit, runCommands, etc)
- [ ] Add single responsibility focus
- [ ] Document in Zeus agents list
- [ ] Document in relevant Planning/Implementation agents
- [ ] Test with sample task
- [ ] Add to memory bank if discovering new patterns

---

## � ARTIFACTS GENERATED BY WORKFLOW

Each Zeus execution creates documented artifacts:

### During Planning Phase
```
plans/<feature-name>/
└── plan.md              (Complete structure, 3-10 phases, TDD roadmap)
```
**Contains:**
- Feature overview and objectives
- Phase-by-phase breakdown with test requirements
- Listed files to create/modify
- Open questions for user
- Risk assessment

### During Implementation Phase (per phase)
```
plans/<feature-name>/
└── phase-N-complete.md  (Result of EACH phase after Temis approval)
```
**Contains:**
- Phase objective and summary
- Files created/modified
- Tests created/passed
- Coverage percentage
- Temis review result (APPROVED/NEEDS_REVISION/FAILED)
- Git commit message
- Decisions made in this phase

### After Completion
```
plans/<feature-name>/
└── complete.md          (Final summary of entire project)
```
**Contains:**
- Total phases completed checklist
- Total coverage percentage
- Complete file impact list
- Key functions/classes added
- Test coverage summary
- Recommendations for next steps

### Benefits of the Artifact Trail
- ✅ **Audit Trail**: Exact review of what was done
- ✅ **Knowledge Transfer**: New team members understand decisions
- ✅ **Project Documentation**: Natural documentation of feature dev
- ✅ **PR Descriptions**: Copy plan.md to your PR
- ✅ **Resumable Work**: If interrupted, continue from any phase

---

## �📚 References

- **Agent Skills:** `.github/skills/*/SKILL.md`
- **Custom Instructions:** `.github/instructions/*-standards.instructions.md`
- **Prompt Files:** `.github/prompts/*.prompt.md`
- **Agent Definitions:** `agents/*.agent.md`
- **Memory Bank:** `/docs/memory-bank/`
- **VSCode Settings:** `.vscode/settings.json`

---

**Last Updated:** February 5, 2026  
**Total Agents:** 9 (1 orchestrator + 8 specialized)  
**Total Skills:** 6  
**Total Custom Instructions:** 5  
**Total Prompt Files:** 6  
**Architecture Pattern:** Conductor-Delegate  
**Mythology Reference:** Greek (Zeus, Athena, Apollo, Hermes, Aphrodite), Egyptian (Ra, Maat, Temis), Greek memory (Mnemosyne)

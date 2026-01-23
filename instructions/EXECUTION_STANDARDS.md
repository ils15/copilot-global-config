---
applyTo: '**'
description: 'Execution Standards - Consolidated rules for code quality, planning, and documentation'
---

# Execution Standards - Ofertasdachina Platform (v4.0)

## 🎯 Core Philosophy

You are an expert AI pair programmer for the Ofertasdachina platform. Your primary goal is to make precise, high-quality, and safe code modifications using the **7-agent generalist system** (product, engineering, quality, ops, security, analyst, memory).

---

## 📋 Critical Execution Rules

### **Rule 0: Code Quality (MANDATORY)**

**4 REGRAS CRÍTICAS OBRIGATÓRIAS:**

- **0.1**: Use `@quality` agent ALWAYS after code changes (every file >20 lines, every feature)
- **0.2**: Use specialized agent to evaluate code:
  - Python/FastAPI → `@engineering`
  - React/TypeScript → `@engineering`
  - Database/SQL → `@ops`
  - Docker/Infrastructure → `@ops`
- **0.3**: Research best practices BEFORE coding:
  - Step 1: `grep_search` for similar patterns in codebase
  - Step 2: Use `@product` to evaluate design options
  - Step 3: Use `@analyst` to research best practices
  - Step 4: Document findings in Memory Bank
  - Step 5: THEN implement with full context
- **0.4**: Remove backward compatibility & legacy code with EVERY modification (see checklist below)

---

### **Rule 1: Planning (MANDATORY)**

Always create **INTERNAL IMPLEMENTATION PLAN** before coding.

**Plan Structure:**
```
GOAL: [1 sentence - what are we building?]
SCOPE: [list of files/functions affected]
JUSTIFICATION: [1 line - why this approach?]
RISKS: [any edge cases or dependencies?]
STEPS:
  1. [specific action]
  2. [specific action]
  3. [specific action]
```

**Requirements:**
- Rule 1.1: Always create plan before coding
- Rule 1.2: Favor simple, readable solutions over clever code
- Rule 1.3: Code must be robust AND well-documented inline
- Rule 1.4: Use async/await for ALL I/O operations
- Rule 1.5: Plan for network failures, API timeouts, external service issues
- Rule 1.6: After implementation, review all modified code for correctness
- Rule 1.7: Execute immediately after plan (no approval needed)

---

### **Rule 2: Code Quality & Architecture**

#### **🚨 CRITICAL: Anti-Monolithic Code**

**NEVER create monolithic scripts or files.**

Mandatory:
- **300-Line Limit**: Files >300 lines MUST be refactored
- **Single Responsibility**: Each function does ONE thing
- **Clear Separation**: Config, logic, utilities in separate modules
- **No God Objects**: Avoid classes/functions doing too many things

#### **🎯 Simplicity & Readability**

Code must be SIMPLE and READABLE:
- **Readable Names**: Clear, descriptive identifiers
- **Obvious Logic**: Simplify instead of complex comments
- **Standard Patterns**: Use well-known patterns, no tricks
- **Inline Documentation**: Comments explaining WHY (not what)
- **Separation of Concerns**: DRY principle, SOLID principles
- **Consistent Naming**: Follow project conventions

#### **Dependency Management**
- Minimal dependencies, version pinning
- Security updates tracked
- Organized imports (stdlib → third-party → local)

---

### **Rule 3: Code Review & Validation**

#### **🚨 ABSOLUTE RULE: Never mark modifications complete without review.**

**Validation Workflow:**

1. **Syntax & Type Checking**
   ```bash
   # Python
   python -m compileall <file.py>  # Syntax
   mypy <file.py>                  # Types
   
   # JavaScript/TypeScript
   tsc --noEmit    # Compiler
   eslint <file.js> # Linting
   ```

2. **Self-Review (MANDATORY)**
   - Read ALL modified lines
   - Verify logic and edge cases
   - Check documentation
   - Analyze impact

3. **Quality Agent Validation**
   - Use `@quality` for changes >3 files or >200 lines
   - Pattern: "Review [file] for correctness, style, patterns"

4. **Integration Validation**
   - Check imports, dependencies, config
   - Test related modules
   - Verify no breaking changes

---

### **Rule 4: Documentation**

**🚨 CRITICAL: NO automatic .md files**

- ✅ **DO**: Document in Memory Bank (/docs/memory-bank/)
- ✅ **DO**: Keep README.md in root (if using custom instructions)
- ✅ **DO**: Write docstrings/comments in code
- ❌ **NEVER**: Create auto-generated .md files (GUIDE.md, SUMMARY.md, CHANGELOG.md, STATUS.md)
- ❌ **NEVER**: Create SESSION-SUMMARY.md, CONSOLIDADO.md, FINAL.md
- ❌ **NEVER**: Create multiple versions of same document
- ❌ **NEVER**: Auto-display file content (no `cat`, no giant outputs >50 lines)

**Documentation Location Rules:**
- Rule 4.1: Core project docs → `/docs/memory-bank/`
- Rule 4.2: Task tracking → `/docs/memory-bank/_tasks/`
- Rule 4.3: Implementation notes → `/docs/memory-bank/_notes/`
- Rule 4.4: Only allowed outside Memory Bank: README.md (if requested), CONTRIBUTING.md, .github/templates

---

### **Rule 5: Task Management**

**Memory Bank Integration (from memory-bank.instructions.md):**

- Rule 5.1: Update Memory Bank after complex implementations
- Rule 5.2: Use `/docs/memory-bank/tasks/_index.md` for tracking all tasks
- Rule 5.3: Create individual task files: `TASKID-taskname.md` for each task
- Rule 5.4: Update both subtask status table and progress log when progressing
- Rule 5.5: Update overall task status, completion %, and _index.md

**Example Task File:**
```markdown
# TASK0001 - Feature Name

**Status**: Not Started | In Progress | Completed  
**Priority**: P0 | P1 | P2  

## Progress

| Subtask | Status | Notes |
|---------|--------|-------|
| 1.1 Design | ✅ Complete | Schema done |
| 1.2 Implement | 🔄 In Progress | 60% |
| 1.3 Tests | ⏳ Pending | - |
```

---

### **Rule 6: Backward Compatibility Removal**

**STRICT RULE: Every code modification must eliminate technical debt.**

**Cleanup Checklist (REQUIRED):**

When modifying code:
- [ ] Search for deprecated patterns in the file
- [ ] Search for backward compatibility workarounds
- [ ] Remove legacy code branches
- [ ] Update imports (remove old paths)
- [ ] Delete unused functions/parameters
- [ ] Simplify conditionals

**Patterns to REMOVE:**

```python
# ❌ REMOVE: Old API endpoint
@app.get("/old/endpoint")  # Legacy, deprecated
def old_endpoint():
    return legacy_response()

# ❌ REMOVE: Backward compat parameter
def process(data, use_old_parser=False):  # False by default → remove param
    if use_old_parser:
        return old_parse(data)  # DELETE BRANCH
    return new_parse(data)

# ❌ REMOVE: Legacy database handling
def migrate_user(old_user):
    # Support old "username" before migration to "login_name"
    name = old_user.get('username') or old_user.get('login_name')  # CLEAN
    return User(login_name=name)
```

**Cleanup Patterns:**
- [ ] No `if legacy_version` checks
- [ ] No `# Old code, keep for backward compat` comments
- [ ] No deprecated parameter flags
- [ ] No `try: new_method() except: old_method()`
- [ ] No old schema migrations referenced
- [ ] No unused imports from old modules

---

### **Rule 7: Error Handling & Logging**

**Strategy:**
- Comprehensive error coverage (no silent failures)
- Graceful degradation (fail predictably)
- User-friendly messages (not tech jargon)
- Sufficient logging context (timestamp, level, context)

**Logging Standards:**
- Structured formats (JSON when possible)
- Appropriate levels (ERROR, WARN, INFO, DEBUG)
- NO sensitive data (no passwords, tokens, PII)
- Performance conscious (don't log in hot loops)

---

### **Rule 8: Security**

#### **Input Validation**
- Validate ALL inputs
- Sanitize data before use
- Use strong typing
- Enforce length limits

#### **Authentication & Authorization**
- Use secure protocols (HTTPS, TLS)
- Apply least privilege principle
- Secure session management
- Protect tokens/credentials

#### **Data Protection**
- Encryption at rest & in transit
- Secure secrets storage
- Minimize PII collection
- Ensure regulatory compliance (LGPD, GDPR)

---

### **Rule 9: Docker & Infrastructure**

#### **Best Practices**
- Minimal images, multi-stage builds
- Non-root user, regular updates
- Layer caching optimization
- Environment variables for config

#### **Dockerfile Standards**
- Consistent patterns across files
- Documented operations
- Size/time optimization
- Build & runtime testing

---

### **Rule 10: Git Best Practices**

#### **Commits**
- Atomic commits (one logical change)
- Descriptive messages (50 char subject + body)
- Frequent commits (multiple commits > one giant commit)
- Clean history

#### **Branching**
- Feature branches from main
- Pull requests for code review
- Appropriate merge strategy (squash vs merge)
- Consistent naming (feature/X, bugfix/X, hotfix/X)

---

### **Rule 11: Deployment & Operations**

#### **Environment Setup**
- Virtual environments per project
- Documented dependencies (requirements.txt, package.json)
- Setup automation (scripts, Docker)

#### **Monitoring & Alerting**
- Health checks on critical services
- Key metrics monitoring (latency, errors, throughput)
- Critical failure alerts

#### **Backup & Recovery**
- Automated daily backups
- Tested restore procedures
- Disaster recovery documentation

---

## ⚠️ CONFLICT RESOLUTION

If rules conflict, apply this priority:
1. **Level 1 (HIGHEST)**: Documentation rules (never override "no auto .md" rule)
2. **Level 2**: Planning rules (MUST create plans before implementation)
3. **Level 3**: Task management (nice-to-have, don't override #1-2)

---

## 🤖 Agent Quick Reference

| Agent | Use | Example |
|-------|-----|---------|
| **@product** | Strategic planning, design decisions, research | "Plan JWT authentication architecture" |
| **@engineering** | Code implementation, quality | "Implement auth service with validation" |
| **@quality** | Code review, testing, validation | "Review auth service for correctness" |
| **@ops** | Deployment, infrastructure, CI/CD | "Deploy auth service to production" |
| **@security** | OWASP audit, threat modeling, vulnerability analysis | "Audit auth service for security issues" |
| **@analyst** | Investigation, RCA, performance analysis | "Debug why auth is slow" |
| **@memory** | Context management, retrospectives, progress tracking | "Update Memory Bank with JWT implementation" |

---

## 📚 Related Documents

- **Main Agents Configuration**: `/agents.md`
- **Agent Profiles**: `/.github/agents/*.md`
- **Memory Bank**: `/docs/memory-bank/`
- **Subagent Rules**: `/subagents.instructions.md`
- **Memory Bank Instructions**: `/memory-bank.instructions.md`

---

**Version**: 4.0 (Official GitHub agents.md format)  
**Last Updated**: January 23, 2026  
**Status**: ✅ Production Ready

---
applyTo: '**'
description: 'GitHub Copilot execution guidelines - code quality, review, and best practices'
---

# GitHub Copilot - Execution Guidelines

## **Core Directive**

You are an expert AI pair programmer for the Ofertasdachina platform. Your primary goal is to make precise, high-quality, and safe code modifications.

**For planning rules, see [00-CORE/core.rules.md](00-CORE/core.rules.md)**

## **Code Quality & Architecture**

### **🚨 CRITICAL: Anti-Monolithic Code Rule**

**NEVER create monolithic scripts or files.**

**Mandatory Rules:**
- **300-Line Limit:** Files >300 lines MUST be refactored
- **Modular Functions:** Single-responsibility functions
- **Clear Separation:** Config, logic, utilities in separate modules
- **No God Objects:** Avoid classes/functions doing too many things

### **🎯 Simplicity & Readability First**

**Code must be SIMPLE and READABLE.**

**Rules:**
- **Readable Names:** Clear, descriptive names
- **Obvious Logic:** Simplify instead of complex comments
- **Standard Patterns:** Well-known patterns, no clever tricks
- **Inline Documentation:** Comments explaining WHY

### **Code Organization**
- Separation of concerns, DRY principle, SOLID principles
- Consistent naming conventions

### **Dependency Management**
- Minimal dependencies, version pinning, security updates
- Organized imports (stdlib, third-party, local)

## **🔒 Code Review & Validation Protocol**

**🚨 ABSOLUTE RULE: Never mark modifications complete without review.**

### **NEW: 4 Critical Workflow Rules**

#### **Rule 1: Always Run Quality Agent After Code Changes**

**Mandatory for EVERY code modification:**
```
1. Make code changes
2. IMMEDIATELY invoke @Quality subagent
3. Quality returns review feedback
4. Address any issues
5. Only then mark task complete
```

**Trigger @Quality for:**
- Any change >1 file
- Any change >20 lines
- Any new feature or bugfix
- Any refactoring

**Command:**
```
Use @Quality subagent to: review [file.py/file.ts] for correctness, style, and patterns
Return: feedback and approval/rejection
```

#### **Rule 2: Use Subagent to Evaluate Generated Code**

**After writing code, ALWAYS evaluate with appropriate subagent:**

| Code Type | Subagent | Evaluation Focus |
|-----------|----------|------------------|
| Python/FastAPI | @Backend | Logic, async patterns, performance |
| React/TypeScript | @Frontend | Component patterns, hooks, state |
| SQL/Migrations | @Database | Schema correctness, migration safety |
| Docker/Linux | @Infra | Best practices, security, optimization |

**Pattern:**
```
1. Write code
2. Invoke subagent: "evaluate [code] for best practices and correctness"
3. Get detailed feedback
4. Fix issues
5. Confirm with subagent (if major changes)
```

#### **Rule 3: Research Best Practices BEFORE Writing Code**

**MANDATORY research phase:**

1. **Understand existing patterns** → Search codebase for similar implementations
2. **Check community standards** → Query documentation for best practices
3. **Review alternatives** → Architect agent evaluates trade-offs
4. **Document decision** → Add note to Memory Bank

**Research Steps:**
```
1. grep_search for similar patterns in codebase
2. Use @Architect to evaluate design options
3. Use @Analyst to research best practices
4. Document findings in 04-active-context.md
5. THEN implement with full context
```

**Example:**
- ❌ WRONG: "Write JWT auth handler"
- ✅ RIGHT: "Research JWT patterns → evaluate trade-offs → implement with validation"

#### **Rule 4: Remove Backward Compatibility & Legacy Code During Any Change**

**STRICT RULE: Every code modification must eliminate technical debt.**

**When modifying code:**
- [ ] Search for deprecated patterns in the file
- [ ] Search for backward compatibility workarounds
- [ ] Remove legacy code branches
- [ ] Update imports (remove old paths)
- [ ] Delete unused functions/parameters
- [ ] Simplify conditionals

**Patterns to REMOVE:**
```python
# ❌ REMOVE: Old API endpoint still supported
@app.get("/old/endpoint")  # Legacy, deprecated in v2
def old_endpoint():
    return legacy_response()

# ❌ REMOVE: Backward compat parameter
def process(data, use_old_parser=False):  # False by default, remove param
    if use_old_parser:
        return old_parse(data)  # DELETE THIS BRANCH
    return new_parse(data)

# ❌ REMOVE: Legacy database column handling
def migrate_user(old_user):
    # Support old "username" field before migration to "login_name"
    name = old_user.get('username') or old_user.get('login_name')  # CLEAN THIS
    return User(login_name=name)
```

**Cleanup Checklist:**
- [ ] No `if legacy_version` checks
- [ ] No `# Old code, keep for backward compat` comments
- [ ] No deprecated parameter flags
- [ ] No `try: new_method() except: old_method()`
- [ ] No old schema migrations referenced
- [ ] No unused imports from old modules

---

### **1. Syntax & Type Checking**

**Python:**
```bash
python -m compileall <file.py>  # Syntax
mypy <file.py>                  # Types
```

**JavaScript/TypeScript:**
```bash
tsc --noEmit    # Compiler
eslint <file.js> # Linting
```

### **2. Self-Review (MANDATORY)**

After changes:
1. Read ALL modified lines
2. Verify logic and edge cases
3. Check documentation
4. Analyze impact

### **3. Subagent Validation**

Use for changes >3 files or >200 lines.

### **4. Integration Validation**

Check imports, dependencies, config.

## **Error Handling & Logging**

### **Strategy**
- Comprehensive error coverage
- Graceful degradation
- User-friendly messages
- Sufficient logging context

### **Logging**
- Structured formats
- Appropriate levels
- No sensitive data
- Performance conscious

## **🔒 Security Guidelines**

### **Input Validation**
- Validate all inputs
- Sanitize data
- Strong typing
- Length limits

### **Authentication & Authorization**
- Secure protocols
- Least privilege
- Secure sessions
- Token protection

### **Data Protection**
- Encryption at rest/transit
- Secure secrets storage
- Minimize PII
- Regulatory compliance

## **🐳 Docker Guidelines**

### **Best Practices**
- Minimal images, multi-stage builds
- Non-root user, regular updates
- Layer caching optimization
- Env vars for config

### **Dockerfile Standards**
- Consistent patterns
- Documented operations
- Size/time optimization
- Build/runtime testing

## **📚 Git Best Practices**

### **Commits**
- Atomic commits
- Descriptive messages
- Frequent commits
- Clean history

### **Branching**
- Feature branches
- Pull requests
- Appropriate merge strategy
- Consistent naming

## **Deployment & Operations**

### **Environment Setup**
- Virtual environments
- Documented dependencies
- Setup automation

### **Monitoring & Alerting**
- Health checks
- Key metrics monitoring
- Critical failure alerts

### **Backup & Recovery**
- Automated backups
- Tested restore procedures
- Disaster recovery documentation
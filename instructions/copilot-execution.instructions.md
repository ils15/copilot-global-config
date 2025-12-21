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

**Never mark modifications complete without review.**

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
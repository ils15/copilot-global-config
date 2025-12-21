---
name: security-audit
description: Audit code for security vulnerabilities using OWASP Top 10, STRIDE threat modeling, and secure coding practices. Identifies SQL injection, XSS, CSRF, auth issues, and secrets exposure. Returns prioritized findings with remediation.
---

# Security Audit Skill

## When to Use

Use this skill when:
- Reviewing code for security vulnerabilities
- Auditing authentication/authorization logic
- Checking for secrets exposure in code
- Validating input sanitization
- Reviewing API security (rate limiting, CORS)
- Assessing database query safety
- Evaluating encryption and hashing

## OWASP Top 10 Checklist

### A01: Broken Access Control
```
✅ Checks:
- [ ] Role-based access control (RBAC) implemented
- [ ] JWT validation on all protected endpoints
- [ ] Authorization checks in service layer
- [ ] No direct object references exposed
- [ ] Admin functions protected
```

### A02: Cryptographic Failures
```
✅ Checks:
- [ ] Passwords hashed with bcrypt/argon2
- [ ] Secrets in environment variables (not code)
- [ ] HTTPS enforced
- [ ] Sensitive data encrypted at rest
- [ ] No hardcoded API keys
```

### A03: Injection
```
✅ Checks:
- [ ] Parameterized SQL queries (SQLAlchemy ORM)
- [ ] Input validation with Pydantic
- [ ] No string concatenation in queries
- [ ] Command injection prevented
- [ ] XSS sanitization on output
```

### A04: Insecure Design
```
✅ Checks:
- [ ] Rate limiting implemented
- [ ] CORS properly configured
- [ ] Error messages don't leak info
- [ ] Defense in depth applied
- [ ] Fail-secure defaults
```

### A07: Authentication Failures
```
✅ Checks:
- [ ] Strong password policy
- [ ] Account lockout after failures
- [ ] Session timeout configured
- [ ] MFA available
- [ ] Secure password reset flow
```

## STRIDE Threat Model

```
S - Spoofing: Can attacker impersonate user?
T - Tampering: Can attacker modify data?
R - Repudiation: Can actions be traced?
I - Information Disclosure: Can data leak?
D - Denial of Service: Can system be crashed?
E - Elevation of Privilege: Can attacker gain admin?
```

## Output Format

```markdown
## Security Audit Report

### Severity Summary
- 🔴 Critical: X findings
- 🟠 High: X findings
- 🟡 Medium: X findings
- 🟢 Low: X findings

### Findings

#### [SEV-001] SQL Injection in user_service.py:45
- **Severity**: Critical
- **OWASP**: A03 Injection
- **Location**: `backend/services/user_service.py:45-50`
- **Issue**: String concatenation in SQL query
- **Remediation**: Use parameterized query
- **Code Fix**:
```python
# Before (vulnerable)
query = f"SELECT * FROM users WHERE id = {user_id}"

# After (secure)
query = select(User).where(User.id == user_id)
```

### Recommendations
1. [Priority 1 fix]
2. [Priority 2 fix]
```

## Example Usage

```
@security Audit the authentication module for vulnerabilities
@security Check for secrets exposure in the codebase
@security Review API endpoints for injection risks
@security Validate CORS configuration
```

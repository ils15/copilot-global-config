---
name: security-audit
description: "Security audit and vulnerability detection - OWASP Top 10, input validation, injection attacks"
---

# Security Audit Skill

## OWASP Top 10 Checks

### 1. Broken Access Control
```python
# ❌ WRONG: No authorization check
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    await db.delete(User, user_id)

# ✅ RIGHT: Check permissions
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, current_user: User):
    if user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "Not authorized")
    await db.delete(User, user_id)
```

### 2. Cryptographic Failures
```python
# ❌ WRONG: Store plain password
user.password = password

# ✅ RIGHT: Hash password
user.password = hashlib.sha256(password.encode()).hexdigest()
# Better: use bcrypt/argon2
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])
user.password = pwd_context.hash(password)
```

### 3. Injection Attacks
```python
# ❌ WRONG: SQL injection
query = f"SELECT * FROM users WHERE email = '{email}'"

# ✅ RIGHT: Parameterized queries
query = select(User).where(User.email == email)
```

### 4. Insecure Design
- Input validation on ALL endpoints
- Rate limiting on sensitive operations
- CSRF tokens for state changes
- CORS properly configured

### 5. Security Misconfiguration
```python
# ❌ WRONG: Debug in production
app = FastAPI(debug=True)

# ✅ RIGHT: Debug only in dev
app = FastAPI(debug=os.getenv("ENVIRONMENT") == "development")
```

### 6. Vulnerable & Outdated Components
- Pin dependencies versions
- Regular security updates
- Audit packages: `pip audit`
- Use dependabot/renovate

### 7. Authentication Failures
```python
# ✅ Best Practice: JWT with expiration
token = jwt.encode(
    {
        "sub": user.id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    },
    SECRET_KEY,
    algorithm="HS256"
)
```

### 8. Software & Data Integrity Failures
- Verify package signatures
- Use HTTPS only
- Sign API responses (when needed)

### 9. Logging & Monitoring Failures
```python
# ✅ Log security events
logger.warning(f"Failed login attempt for {email}")
logger.error(f"SQL error encountered: {error_code}")
# BUT: Never log passwords, tokens, PII!
```

### 10. Server-Side Request Forgery (SSRF)
- Validate URLs before fetching
- Whitelist allowed domains
- Disabled redirects to internal IPs

## Checklist
- [ ] All inputs validated
- [ ] Passwords hashed (bcrypt/argon2)
- [ ] No hardcoded secrets
- [ ] CORS configured properly
- [ ] Rate limiting active
- [ ] Errors don't leak info
- [ ] HTTPS only
- [ ] Security headers set

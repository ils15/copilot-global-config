---
name: review-code
description: "Comprehensive code review with security audit, test coverage analysis, and quality gates"
argument-hint: "[Files to review or PR description]"
agent: athena-subagent
tools: ['search', 'usages']
---

# Revisar Código com Segurança (Têmis)

## Review Checklist

### Correctness (CRITICAL)
- [ ] Logic correto e completo
- [ ] Edge cases tratados
- [ ] Error handling apropriado
- [ ] Performance aceitável
- [ ] Sem OWASP vulnerabilities

### Code Quality
- [ ] Sem duplicação (DRY)
- [ ] Single responsibility functions
- [ ] Naming claro
- [ ] Reasonable complexity
- [ ] File size apropriado

### Architecture & Design
- [ ] Segue design patterns
- [ ] Proper separation of concerns
- [ ] Dependencies bem gerenciadas
- [ ] Extensibilidade considerada
- [ ] Consistência com codebase

### Testing
- [ ] Unit tests escritos
- [ ] >80% coverage
- [ ] Integration tests existem
- [ ] Edge cases testados
- [ ] Error conditions testados

### Documentation
- [ ] Funções públicas documentadas
- [ ] Comments explicam WHY
- [ ] README/guides acurados
- [ ] API docs completos
- [ ] Assumptions documentadas

### Security (OWASP)
- [ ] Input validation present
- [ ] Sem hardcoded secrets
- [ ] Secure dependencies
- [ ] No XXE, CSRF, XSS
- [ ] Auth/authz corretos
- [ ] Encryption para dados sensíveis
- [ ] Session/token management
- [ ] Rate limiting
- [ ] Audit logging

## Feedback Format

**Result**: APPROVED | NEEDS_REVISION | FAILED

**Issues by Severity**:
- 🔴 CRITICAL: Security, data loss, breaking change
- 🟠 HIGH: Correctness, performance problem
- 🟡 MEDIUM: Code quality, maintainability
- 🟢 LOW: Style, non-critical

## When to Use
- Antes de merge para main
- Security audits
- Verificar compliance

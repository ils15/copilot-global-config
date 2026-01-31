---
description: "Code review standards and security audit guidelines"
name: "Code Review & Security Standards"
applyTo: "**"
---

# Code Review Standards (Têmis)

## Review Scope
- Review ONLY changed files
- Check diff, não arquivo inteiro
- Revisar commits relacionados
- Link para related PRs/issues

## Correctness
- Logic é correto e completo
- Edge cases tratados
- Error handling apropriado
- Performance aceitável

## Code Quality
- No duplicação (DRY principle)
- Single responsibility functions
- Naming claro e descritivo
- Reasonable complexity
- Proper file sizes

## Testing
- Unit tests escritos
- >80% code coverage
- Integration tests para workflows
- Edge cases testados
- Error conditions testados

## Security (OWASP Top 10)
- Input validation present
- Sem hardcoded secrets/credentials
- Secure dependencies
- No XXE, CSRF, XSS vulnerabilities
- Authentication/authorization proper
- Encryption para dados sensíveis
- Session/token management seguro
- Rate limiting em endpoints sensitivos
- Audit logging para eventos de security

## Documentation
- Public functions documented
- Comments explicam WHY não WHAT
- README/guides acurados
- API documentation completa

## Feedback Format
- Return: APPROVED | NEEDS_REVISION | FAILED
- Categorize: CRITICAL | HIGH | MEDIUM | LOW
- Provide specific file:line references
- Suggest solutions or alternatives

---
name: implement-feature
description: "Implement a complete feature end-to-end with TDD, parallel execution, and quality gates"
argument-hint: "[Brief feature description]"
agent: zeus
tools: ['search', 'usages', 'edit', 'runCommands', 'runTasks']
---

# Implementar Feature com TDD (Zeus Orchestration)

## Workflow Completo (5 Fases)

### Fase 1 - Planning (@Métis)
Use @metis-subagent para:
- Pesquisar arquitetura existente
- Criar plano TDD detalhado 3-10 fases
- Analisar riscos e mitigações
- Oferecer handoff automático

### Fase 2 - Parallel Implementation
Confira qual combinar (backend, frontend, database):
- @hermes-subagent → Backend APIs & services (FastAPI)
- @afrodite-subagent → Frontend components (React/TypeScript)
- @tethys-subagent → Database migrations (SQLAlchemy)

**Executar em paralelo!** Isso reduz tempo em 60%.

### Fase 3 - Quality Gate (@Têmis)
- Revisar APENAS arquivos alterados
- Verificar: OWASP Top 10, cobertura >80%, TDD seguido
- Retornar: APPROVED | NEEDS_REVISION | FAILED

### Fase 4 - Integration Testing
- Testar workflows end-to-end
- Verificar data consistency
- Performance testing

### Fase 5 - Deployment (@Rá)
- Deploy para staging
- Health checks
- Smoke tests
- Deploy para production

## Success Criteria
✅ Tests pass (>80% coverage)
✅ Code reviewed & approved
✅ No OWASP vulnerabilities
✅ Performance acceptable
✅ Documentation updated
✅ Deployed successfully

## When to Use
- Implementar nova feature complexa
- Quando você quer QA automático
- Para coordenar trabalho paralelo

---
description: "Backend development standards for FastAPI/Python APIs"
name: "Backend Development Standards"
applyTo: "**/*.py"
---

# Backend Development Standards (Hermes)

## Async/Await
- Use async/await para TODAS operações I/O (database, external APIs, file operations)
- Nunca sincronizar o que é assíncrono
- Use `asyncio.gather()` para operações paralelas

## Test-Driven Development
- RED: Escrever teste que falha
- GREEN: Código mínimo para passar
- REFACTOR: Melhorar sem quebrar testes

## Type Safety
- Type hints em todos parâmetros de função
- Type hints em todos return types
- Use Pydantic para request/response validation

## Code Organization
- Máximo 300 linhas por arquivo
- Separe: routes → services → models
- Docstrings em funções públicas (Google format)

## Error Handling
- Nunca silent failures (catch e log)
- Use HTTP status codes apropriados
- Retorne mensagens de erro amigáveis (sem stack traces)
- Implemente retry logic com exponential backoff

## Performance
- Evite N+1 queries (use eager loading/joins)
- Implementar pagination para list endpoints
- Cache para dados frequentemente acessados
- Monitor async deadlocks

## Security
- Input validation em todas endpoints
- CSRF protection
- Rate limiting para endpoints sensitivos
- Sanitize logs (nunca log senhas/tokens)

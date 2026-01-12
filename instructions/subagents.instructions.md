---
applyTo: '**'
description: 'Subagent Rules - Direct and Efficient'
---

# Subagent Rules

## Quando Usar Subagente

✅ Use quando:
- Análise de >5 arquivos
- Tarefa complexa com múltiplos passos
- Research que precisa de contexto isolado

❌ Não use quando:
- Tarefa simples (<50 linhas)
- 1-2 arquivos
- Quick fix

## Como Invocar

```
Use @Backend subagent to: [tarefa específica em 1 linha]
Return: [formato esperado: code/list/table]
```

## Regras para Subagentes

1. **Tarefa específica** - 1 linha, sem ambiguidade
2. **Output direto** - código ou resultado, sem explicação
3. **Sem documentação** - nunca criar .md (handoff to @Planner for Memory Bank updates)
4. **Máximo 1 nível** - subagente não invoca outro subagente

### 🚨 Documentação Rule (CRITICAL)

**NUNCA criar qualquer arquivo .md** - Subagentes NEVER criam documentação. 

Se precisar atualizar Memory Bank:
```
Use @Planner to: Update Memory Bank with these changes [brief description]
Return: Confirmation of Memory Bank updates
```

Referência: [memory-bank.instructions.md](memory-bank.instructions.md)

## Exemplo

```
Use @Backend subagent to: fix the authentication bug in auth_service.py
Return: patched code only
```

## Agentes Disponíveis

| Agente | Uso |
|--------|-----|
| @Backend | Python, FastAPI, async |
| @Frontend | React, TypeScript, Next.js |
| @Database | SQL, Alembic, migrations |
| @Infra | Docker, Traefik, deploy |
| @Analyst | Research, debugging |
| @Quality | Code review, tests |
| @Planner | Task planning |

---

Regra principal: **DIRETO E CURTO**

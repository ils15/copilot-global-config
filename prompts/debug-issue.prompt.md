---
name: debug-issue
description: "Rapidly debug issues with parallel file discovery and analysis"
argument-hint: "[Error message or bug description]"
agent: apollo-subagent
tools: ['search', 'usages']
---

# Debug Rápido (Apollo - Scout)

## 5-10 Parallel Searches

Apollo lança buscas paralelas simultâneas:

Search 1: Mensagem de erro exata
Search 2: Função/classe mencionada
Search 3: File patterns relacionados
Search 4: Test cases similares
Search 5: Related issues/PRs
Search 6: Stack trace patterns
Search 7: Config files
Search 8: Logging statements
Search 9: Dependencies mentioned
Search 10: Recent changes em area

## Analysis & Synthesis
- Elimina duplicatas
- Identifica file relationships
- Extrai padrões
- Retorna achados prioritizados

## Recommendations

After analysis, @apollo retorna:
1. **Root Cause Hypothesis**: O que provavelmente está errado
2. **Key Files**: Arquivos mais relevantes
3. **Reproduction Steps**: Como reproduzir
4. **Suggested Fix**: Direção de solução
5. **Next Steps**: Próximas agentes para envolver

## When to Use
- Bug report recebido
- Error stack trace confuso
- Performance issue diagnosis
- Regression debugging
- Quando precisa exploração rápida

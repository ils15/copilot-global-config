---
applyTo: '**'
description: 'Guia completo para preencher, manter e gerenciar Memory Banks'
---

# 📚 Guia de Instruções - Memory Banks

## **1. Estrutura Padrão de Memory Bank**

Cada Memory Bank deve ter EXATAMENTE estes 7 arquivos (+ pasta `tasks/`):

```
memory-bank-{service}/
├── 00-overview.md           # O que é? Por quê? Como funciona? COMECE AQUI
├── 01-architecture.md       # Design, componentes, fluxos, diagramas
├── 02-components.md         # Módulos, classes, funções, APIs internas
├── 03-process.md            # Workflows, algoritmos, lógica de negócio
├── 04-active-context.md     # Estado atual, decisões ativas, próximos passos
├── 05-progress-log.md       # Histórico de mudanças, quando/o quê foi feito
├── 06-deployment.md         # Deploy, startup, monitoramento, troubleshooting
├── 07-reference.md          # Links externos, recursos, APIs de terceiros
└── tasks/
    ├── _index.md            # Índice de todas as tarefas
    ├── TASK001-taskname.md
    ├── TASK002-taskname.md
    └── ...
```

**✅ REGRA CRÍTICA**: Usar APENAS este padrão. Nenhum arquivo extra fora dessa estrutura.

---

## **2. O Que Colocar em Cada Arquivo**

### **00-overview.md** (Visão Geral)
**Propósito**: Seu "README" - primeira coisa que alguém lê

**Seções obrigatórias**:
```markdown
# Overview - [Service Name]

## O que é?
[Descrição breve: 2-3 linhas do que é este serviço]

## Por quê existe?
[O problema que resolve]

## Como funciona?
[Visão de alto nível do fluxo]

## Arquitetura em 30 segundos
[Diagrama ASCII simples ou descrição muito breve]

## Arquivo? Comece aqui →
- 👤 Iniciante: 01-architecture.md
- 🔧 Desenvolvedor: 02-components.md
- 🚀 DevOps: 06-deployment.md

## Estrutura de pastas
[Hierarquia de diretórios importantes]

## Status atual
[Pronto para produção / Em desenvolvimento / Parcial]
```

**Exemplo mínimo**: ~200 linhas

---

### **01-architecture.md** (Arquitetura)
**Propósito**: Entender o design e fluxos

**Seções obrigatórias**:
```markdown
# Architecture - [Service Name]

## Design High-Level
[Diagrama ASCII ou descrição]

## Componentes principais
- Componente A: [o quê faz]
- Componente B: [o quê faz]

## Fluxos principais
### Fluxo 1: [Descrição]
[Diagrama de sequência em ASCII ou passo a passo]

### Fluxo 2: [Descrição]
[...]

## Dependências externas
- Banco de dados: [qual]
- APIs externas: [quais]
- Serviços internos: [quais]

## Decisões arquiteturais
1. [Decisão] - Por quê?
2. [Decisão] - Por quê?

## Ver também
→ 02-components.md para detalhe técnico
→ 03-process.md para workflows
```

**Exemplo mínimo**: ~300-400 linhas

---

### **02-components.md** (Componentes/Código)
**Propósito**: Mapa técnico detalhado (sem copiar código inteiro)

**Seções obrigatórias**:
```markdown
# Components - [Service Name]

## Estrutura de arquivos
```
service/
├── src/
│   ├── main.py/index.js        [o quê faz]
│   ├── models/                  [modelos de dados]
│   ├── services/                [lógica de negócio]
│   └── api/                     [rotas/endpoints]
└── tests/                       [testes]
```

## Principais classes/funções
### [Class/Function Name]
- **Arquivo**: path/to/file.py
- **Propósito**: o quê faz
- **Responsabilidades**: lista
- **Entradas**: tipos
- **Saídas**: tipos
- **Exemplo de uso**: [snippet MUITO pequeno]

## APIs/Endpoints
| Método | Path | Descrição | Auth |
|--------|------|-----------|------|
| GET | /api/endpoint | o quê faz | JWT |
| POST | /api/endpoint | o quê faz | API Key |

## Banco de dados
### Tabelas principais
- `users`: campos, índices
- `offers`: campos, índices

## Configuração
- Variáveis de ambiente obrigatórias
- Valores padrão
- Secrets necessários

## Ver também
→ 01-architecture.md para design
→ 03-process.md para fluxos
→ 04-active-context.md para mudanças recentes
```

**Exemplo mínimo**: ~400-500 linhas

---

### **03-process.md** (Processos/Workflows)
**Propósito**: Como coisas acontecem - fluxos detalhados

**Seções obrigatórias**:
```markdown
# Process - [Service Name]

## Fluxos principais

### Fluxo 1: [Descrição]
```
Usuário → Sistema → Banco de dados → Resposta
  ↓         ↓          ↓              ↓
[steps]  [steps]    [steps]        [steps]
```

**Passo 1**: o quê acontece
**Passo 2**: o quê acontece
**Passo 3**: o quê acontece

### Fluxo 2: [Descrição]
[...]

## Algoritmos importantes
### [Nome do algoritmo]
**Entrada**: 
**Processamento**: passo a passo
**Saída**:
**Complexidade**: O(n)
**Casos especiais**: 

## Estados e transições
```
[Estado A] → [Estado B] → [Estado C]
   ↓ erro      ↓ sucesso    ↓ retry
[Falha]     [Sucesso]    [Estado A]
```

## Tratamento de erros
- Se erro X: então faz Y
- Se erro Z: então faz W

## Performance
- Gargalos conhecidos
- Otimizações implementadas
- Métricas esperadas

## Ver também
→ 01-architecture.md para design
→ 02-components.md para código
```

**Exemplo mínimo**: ~300-400 linhas

---

### **04-active-context.md** (Contexto Ativo)
**Propósito**: O que está acontecendo AGORA

**Seções obrigatórias**:
```markdown
# Active Context - [Service Name]

## Data: [YYYY-MM-DD]

## Foco atual
[O que está sendo feito agora em 1-2 linhas]

## Decisões ativas
- [Decisão 1]: porque...
- [Decisão 2]: porque...

## Tarefas em andamento
- [ ] Tarefa 1 - Descrição
- [ ] Tarefa 2 - Descrição

## Bloqueadores
- [Bloqueador 1]: o que bloqueia, próximo passo
- [Bloqueador 2]: o que bloqueia, próximo passo

## Mudanças recentes
- [Data]: o quê mudou
- [Data]: o quê mudou

## Próximos passos
1. [Ação 1]
2. [Ação 2]
3. [Ação 3]

## Referências úteis
→ Ver tasks/_index.md para tarefas em andamento
→ Ver 05-progress-log.md para histórico completo
```

**Mantém**: Atualizar a cada 1-2 semanas ou quando mudança significativa

---

### **05-progress-log.md** (Histórico)
**Propósito**: Registro histórico de tudo que mudou

**Formato**:
```markdown
# Progress Log - [Service Name]

## [Data] - [Versão/Iteração]
**Quem**: [seu nome]
**Foco**: o quê foi feito

### Mudanças
- ✅ Implementado: [o quê]
- ✅ Corrigido: [o quê]
- ✅ Refatorado: [o quê]
- 📝 Documentado: [o quê]

### Testes
- ✅ [Teste 1]
- ✅ [Teste 2]

### Próximas etapas
- [ ] [Próximo passo]
- [ ] [Próximo passo]

### Notas
[Observações importantes]

---

## [Data anterior] - [Versão anterior]
[...)
```

**Mantém**: Adicionar entrada a cada semana de trabalho

---

### **06-deployment.md** (Deploy/Monitoramento)
**Propósito**: Como rodar, monitorar, troubleshoot

**Seções obrigatórias**:
```markdown
# Deployment - [Service Name]

## Build
### Local
```bash
# Pré-requisitos
pip install -r requirements.txt

# Build
docker build -t service-name .

# Verificar
docker images | grep service-name
```

### CI/CD
[Como seu CI/CD faz o build]

## Startup
### Local
```bash
docker run -p 8000:8000 service-name
```

### Produção
```bash
docker-compose -f docker-compose.yml up service-name
```

### Health checks
```bash
curl http://localhost:8000/health
```

## Monitoramento
### Logs
```bash
docker logs -f container-name
```

### Métricas
- CPU: normal < 50%
- Memória: normal < 512MB
- Resposta: < 500ms

## Troubleshooting

### Problema 1: [Descrição]
**Sintomas**: o quê acontece
**Causa**: por quê acontece
**Solução**:
```bash
[comandos]
```

### Problema 2: [Descrição]
**Sintomas**: 
**Causa**: 
**Solução**:

## Rollback
```bash
docker-compose down
docker image rm old-image
git revert [commit]
docker-compose up
```

## Documentação de referência
→ 02-components.md para env vars
→ 04-active-context.md para estado atual
```

**Exemplo mínimo**: ~300-400 linhas

---

### **07-reference.md** (Referências)
**Propósito**: Links, APIs, recursos externos

**Seções obrigatórias**:
```markdown
# Reference - [Service Name]

## Links úteis
- [Nome]: URL - [o que é]
- [Nome]: URL - [o que é]

## APIs internas
- API 1: url, auth, documentação
- API 2: url, auth, documentação

## APIs externas integradas
- [Serviço]: URL, endpoints usados, auth necessária

## Dependências
- [Biblioteca]: versão, para quê
- [Ferramenta]: versão, para quê

## Documentação externa
- [Recurso]: link - [contexto]

## Contatos
- [Pessoa]: responsável por [aspecto], contato

## Ver também
→ 00-overview.md para iniciar
→ 06-deployment.md para troubleshooting
```

---

## **3. Estrutura de Tarefas (tasks/)**

### **3.1 Índice de Tarefas - `_index.md`**

```markdown
# Tasks Index - [Service Name]

## Em Andamento
- [TASK001] Implementar autenticação - 50% completo
- [TASK003] Melhorar performance - Aguardando review

## Pendentes
- [TASK005] Adicionar testes - Planejado para próxima sprint
- [TASK006] Documentar APIs - Backlog

## Completadas
- [TASK002] Setup inicial - Completado em 2025-11-10
- [TASK004] Deploy to staging - Completado em 2025-11-12

## Abandonadas
- [TASK099] Legacy migration - Abandonado (API deprecada)
```

### **3.2 Arquivo de Tarefa Individual - `TASKXXX-taskname.md`**

```markdown
# [TASK ID] - [Task Name]

**Status**: [Pending/In Progress/Completed/Blocked/Abandoned]
**Prioridade**: [Baixa/Média/Alta/Crítica]
**Assignee**: [Nome]
**Data criação**: [YYYY-MM-DD]
**Atualizado**: [YYYY-MM-DD]

## Descrição Original
[O que foi pedido originalmente]

## Contexto
[Por quê esta tarefa existe? Qual problema resolve?]

## Escopo
[O quê está incluído nesta tarefa]

## Critério de Aceição
- [ ] [Critério 1]
- [ ] [Critério 2]
- [ ] [Critério 3]

## Plano de Implementação
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

## Progresso

| Subtarefa | Status | % | Atualizado | Notas |
|-----------|--------|---|----------|-------|
| 1. [Descrição] | In Progress | 50% | 2025-11-15 | Aguardando API key |
| 2. [Descrição] | Pending | 0% | 2025-11-10 | Bloqueado por TASK001 |
| 3. [Descrição] | Complete | 100% | 2025-11-14 | Testes passando |

## Histórico
### 2025-11-15 - Progress update
- Implementado endpoint POST /api/v1/endpoint
- 4 testes novos adicionados
- Documentação atualizada
- **Próximo**: Integração com cache Redis

### 2025-11-14 - Iniciado
- Setup inicial
- Branches criados
- Desenvolvimento começado

## Arquivos afetados
- `src/services/service.py`
- `tests/test_service.py`
- `docs/memory-bank-{service}/01-architecture.md`

## Testes
```bash
# Executar testes
pytest tests/test_task.py -v
```

## Bloqueadores
- Nenhum no momento

## Notas
[Observações importantes]

## Ver também
→ memory-bank-{service}/05-progress-log.md
→ memory-bank-{service}/04-active-context.md
```

---

## **4. Como Preencher (Passo a Passo)**

### **Criar um Memory Bank Novo**

```bash
# 1. Criar diretório
mkdir -p docs/memory-bank-{service}/tasks

# 2. Criar arquivos padrão (cópia dos templates)
cp docs/memory-bank-infrastructure/00-overview.md \
   docs/memory-bank-{service}/00-overview.md

# 3. Editar cada arquivo com conteúdo específico do serviço

# 4. Criar arquivo de índice de tarefas
cat > docs/memory-bank-{service}/tasks/_index.md << 'EOF'
# Tasks Index - [Service Name]

## Em Andamento
(vazio por enquanto)

## Pendentes
(vazio por enquanto)

## Completadas
(vazio por enquanto)
EOF
```

### **Adicionar Nova Tarefa**

```bash
# 1. Criar arquivo de tarefa
cat > docs/memory-bank-{service}/tasks/TASK001-feature-name.md << 'EOF'
# TASK001 - Feature Name

**Status**: Pending
**Prioridade**: Média
**Assignee**: Seu nome
**Data criação**: 2025-11-16

[Preencher seções conforme template acima]
EOF

# 2. Atualizar _index.md
# Adicionar: - [TASK001] Feature Name - Descrição breve

# 3. Atualizar 04-active-context.md
# Adicionar tarefa à seção "Tarefas em andamento"
```

### **Atualizar Progresso de Tarefa**

**Quando fazer**: A cada dia de trabalho na tarefa, pelo menos

1. Abrir arquivo da tarefa: `docs/memory-bank-{service}/tasks/TASKXXX-name.md`
2. Atualizar tabela de progresso (% completo)
3. Adicionar nova entrada em "Histórico"
4. Atualizar status se necessário
5. Executar testes e confirmar critérios
6. Se completo → Status = "Complete" em _index.md

### **Consolidar Tarefa Completa no Progress Log**

Quando uma tarefa está 100% completa:

1. Abrir: `docs/memory-bank-{service}/tasks/TASKXXX-name.md`
2. Marcar **Status = Completed**
3. Abrir: `docs/memory-bank-{service}/05-progress-log.md`
4. Adicionar resumo final (o quê foi feito)
5. Atualizar: `docs/memory-bank-{service}/tasks/_index.md`
6. Mover tarefa para seção "Completadas"

---

## **5. Regras de Ouro**

### ✅ DO (Faça)
- ✅ Atualizar progress log a cada semana de trabalho
- ✅ Manter apenas os 7 arquivos padrão + tasks/
- ✅ Adicionar diagrama ASCII simples quando explicar fluxo
- ✅ Linkar para outros arquivos do mesmo memory bank
- ✅ Usar exemplos de código reais (não conceitual)
- ✅ Atualizar 04-active-context.md quando estado muda
- ✅ Manter tarefas granulares (máximo 1-2 semanas cada)

### ❌ DON'T (Não faça)
- ❌ Criar arquivos fora do padrão 00-07 + tasks/
- ❌ Copiar e colar código inteiro (referência + snippet)
- ❌ Deixar tarefas sem status definido
- ❌ Esquecer de atualizar _index.md depois de mudar status
- ❌ Misturar conceitos de múltiplos memory banks em um arquivo
- ❌ Deixar seções vazias sem comentário (remova ou adicione TBD)
- ❌ Documentar sem vincular a código real

---

## **6. Exemplo Completo - Criar Memory Bank de Novo Serviço**

```bash
# 1. Criar estrutura
mkdir -p docs/memory-bank-newservice/tasks

# 2. Criar 00-overview.md
cat > docs/memory-bank-newservice/00-overview.md << 'EOF'
# Overview - New Service

## O que é?
API que integra com serviço externo para processar dados.

## Por quê existe?
Reduz carga no serviço principal, permitindo processamento assíncrono.

## Como funciona?
1. Recebe requisição
2. Enfileira processamento
3. Processa em background
4. Retorna resultado

## Status
🟡 Em desenvolvimento

## Arquivo? Comece aqui →
- 👤 Iniciante: 01-architecture.md
- 🔧 Desenvolvedor: 02-components.md
EOF

# 3. Criar arquivos 01-07 (copiar templates e adaptar)

# 4. Criar tasks/_index.md vazio

# 5. Criar TASK001
mkdir -p docs/memory-bank-newservice/tasks
cat > docs/memory-bank-newservice/tasks/TASK001-setup.md << 'EOF'
# TASK001 - Setup Inicial

**Status**: In Progress
**Prioridade**: Alta
**Data**: 2025-11-16

## Critério de Aceição
- [ ] Código base criado
- [ ] Estrutura de pasta pronta
- [ ] Ambiente local rodando
- [ ] README escrito

## Progresso

| Subtarefa | Status |
|-----------|--------|
| 1. Código base | Complete |
| 2. Setup local | In Progress |

## Histórico
### 2025-11-16
- ✅ Criado repo
- 🔄 Configurando venv
EOF

# 6. Atualizar _index.md
cat > docs/memory-bank-newservice/tasks/_index.md << 'EOF'
# Tasks Index - New Service

## Em Andamento
- [TASK001] Setup Inicial - 50% completo

## Pendentes
(vazio)

## Completadas
(vazio)
EOF
```

---

## **7. Manutenção Contínua**

### **Semanal**
- [ ] Atualizar 04-active-context.md com progresso
- [ ] Adicionar entrada em 05-progress-log.md

### **Quando termina tarefa**
- [ ] Marcar TASK como Complete em _index.md
- [ ] Adicionar resumo em 05-progress-log.md
- [ ] Atualizar 04-active-context.md

### **Mensal**
- [ ] Revisar 01-architecture.md se teve mudanças maiores
- [ ] Revisar 02-components.md se nova estrutura adicionada
- [ ] Consolidar múltiplas entradas do progress log se muitas

### **Anual / Big Release**
- [ ] Revisar e atualizar ALL 7 arquivos
- [ ] Garantir nada ficou desatualizado
- [ ] Atualizar status geral em 00-overview.md

---

## **8. Checklist - Memory Bank Completo**

Usar este checklist para validar se seu memory bank está bom:

```markdown
### Validação de Memory Bank

- [ ] 00-overview.md existe e tem ~200 linhas
- [ ] 01-architecture.md existe e tem diagramas
- [ ] 02-components.md existe e mapeia estrutura real
- [ ] 03-process.md existe com fluxos principais
- [ ] 04-active-context.md atualizado (< 1 semana)
- [ ] 05-progress-log.md tem entradas recentes
- [ ] 06-deployment.md tem comandos testados
- [ ] 07-reference.md tem links e recursos
- [ ] tasks/_index.md existe
- [ ] Nenhum arquivo fora do padrão 00-07 + tasks/
- [ ] Todos os arquivos têm cross-references
- [ ] Status geral está claro em 00-overview.md
```

---

**RESUMO**: Structure → Content → Maintain = Memory Bank ✨

# GitHub Copilot - Configurações Globais

Este diretório contém configurações reutilizáveis do GitHub Copilot para uso em múltiplos projetos.

## 📁 Estrutura

```
/home/admin/.github/
├── agents/              # Agentes especializados (backend, frontend, database, etc.)
├── instructions/        # Instruções globais e diretrizes
├── chatmodes/          # Modos de chat personalizados
└── sync-copilot-config.sh  # Script de sincronização
```

## 🔧 Como usar em um projeto

### Opção 1: Symlinks (Recomendado)

Use o script de sincronização para criar links simbólicos:

```bash
cd /seu/projeto
bash /home/admin/.github/sync-copilot-config.sh
```

Ou manualmente:
```bash
cd /seu/projeto
mkdir -p .github
ln -s /home/admin/.github/agents .github/agents
ln -s /home/admin/.github/instructions .github/instructions
ln -s /home/admin/.github/chatmodes .github/chatmodes
```

### Opção 2: Cópia

Se preferir ter uma cópia local (não sincronizada):

```bash
cp -r /home/admin/.github/agents /seu/projeto/.github/
cp -r /home/admin/.github/instructions /seu/projeto/.github/
cp -r /home/admin/.github/chatmodes /seu/projeto/.github/
```

## 📝 Agentes Disponíveis

- **backend** - FastAPI, Python, async, services, repositories
- **frontend** - React, TypeScript, Next.js, UI components, hooks
- **database** - SQL, Alembic migrations, query optimization, schemas
- **docker** - Docker, Docker Compose, container management
- **github** - Git operations, commits, push, pull requests
- **linux** - System administration, bash scripting, CLI tools
- **infra** - Deployment, nginx, Traefik, hot reload
- **debug** - Debugging systematically: reproduce, diagnose, fix
- **reviewer** - Code review, validation, testing, Playwright E2E
- **planner** - Plan features, manage Memory Bank and TODO
- **documentation** - Documentation, Memory Bank, API docs

## 🎯 Instruções Disponíveis

- **copilot-instructions.md** - Instruções principais do Copilot
- **context-isolated-subagents.instructions.md** - Gestão de subagentes
- **memory-bank.instructions.md** - Sistema de Memory Bank
- **memory-bank-guidelines.md** - Diretrizes do Memory Bank
- **no-unnecessary-files.instructions.md** - Evitar arquivos desnecessários
- **project-context.instructions.md** - Contexto de projeto
- **impressao3d-versioning.instructions.md** - Versionamento específico

## 🔄 Atualização

Quando usar symlinks, todas as atualizações em `/home/admin/.github` são refletidas automaticamente em todos os projetos vinculados.

## 🚀 Vantagens

- ✅ Configuração única, uso múltiplo
- ✅ Atualizações centralizadas
- ✅ Consistência entre projetos
- ✅ Fácil manutenção
- ✅ Backup simplificado

## 💾 Backup

Para fazer backup das configurações:

```bash
tar -czf copilot-config-backup-$(date +%Y%m%d).tar.gz /home/admin/.github/
```

## 🔗 Git

Adicione ao `.gitignore` do projeto se usar symlinks:

```gitignore
# GitHub Copilot - usando configurações globais via symlink
.github/agents
.github/instructions
.github/chatmodes
```

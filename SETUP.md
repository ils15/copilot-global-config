# 🚀 Setup - GitHub Copilot Global Config

## 📤 Subindo para o GitHub

### Passo 1: Criar repositório no GitHub

1. Acesse https://github.com/new
2. Nome: `copilot-global-config` (ou outro nome)
3. Descrição: "GitHub Copilot agents and instructions for reuse across projects"
4. **Público** ou **Privado** (você escolhe)
5. **NÃO marque** "Initialize with README" (já temos)
6. Clique em "Create repository"

### Passo 2: Conectar repositório local ao GitHub

```bash
cd /home/admin/.github

# Adicionar remote (substitua SEU_USERNAME)
git remote add origin https://github.com/SEU_USERNAME/copilot-global-config.git

# Ou com SSH (se configurado)
git remote add origin git@github.com:SEU_USERNAME/copilot-global-config.git

# Push inicial
git push -u origin main
```

## 🔧 Usando em outros projetos

### Opção 1: Git Submodule (Recomendado para versionamento)

```bash
cd /seu/projeto

# Adicionar como submodule
git submodule add https://github.com/SEU_USERNAME/copilot-global-config.git .github-global

# Criar symlinks
ln -s .github-global/agents .github/agents
ln -s .github-global/instructions .github/instructions
ln -s .github-global/chatmodes .github/chatmodes

# Commit
git add .gitmodules .github-global .github
git commit -m "chore: add Copilot global config as submodule"
```

### Opção 2: Clone direto (mais simples)

```bash
# Clone o repo globalmente (uma vez por máquina)
git clone https://github.com/SEU_USERNAME/copilot-global-config.git /home/admin/.github-shared

# Em cada projeto, use o script
cd /seu/projeto
bash /home/admin/.github-shared/sync-copilot-config.sh
```

### Opção 3: Symlink direto (desenvolvimento local)

```bash
cd /seu/projeto
bash /home/admin/.github/sync-copilot-config.sh
```

## 🔄 Atualizando configurações

### Quando fizer mudanças locais:

```bash
cd /home/admin/.github
git add .
git commit -m "feat: add new agent for X"
git push
```

### Para atualizar em outros projetos (submodule):

```bash
cd /seu/projeto
git submodule update --remote .github-global
```

## 🌐 Compartilhando com equipe

### README sugerido para time:

```markdown
# Configurações do Copilot

Este projeto usa configurações globais do Copilot.

## Setup inicial

\`\`\`bash
git submodule update --init
bash .github-global/sync-copilot-config.sh
\`\`\`

## Agentes disponíveis
- @backend - FastAPI, Python, async
- @frontend - React, TypeScript, Next.js
- @database - SQL, Alembic, query optimization
- (ver lista completa em .github-global/README.md)
\`\`\`
```

## 📦 Estrutura final no projeto

```
seu-projeto/
├── .github/
│   ├── agents/       -> symlink para .github-global/agents/
│   ├── instructions/ -> symlink para .github-global/instructions/
│   └── chatmodes/    -> symlink para .github-global/chatmodes/
├── .github-global/   (submodule ou clone)
│   ├── agents/
│   ├── instructions/
│   ├── chatmodes/
│   └── README.md
└── .gitignore        (adicionar .github/* se usar symlinks)
```

## 🔐 .gitignore recomendado

Adicione ao `.gitignore` do projeto:

```gitignore
# GitHub Copilot - configurações via submodule/symlink
.github/agents
.github/instructions
.github/chatmodes
```

## ⚡ Quick Start (novo projeto)

```bash
# 1. Clone este repo globalmente
git clone https://github.com/SEU_USERNAME/copilot-global-config.git ~/.copilot-config

# 2. Adicione alias ao ~/.bashrc
echo 'alias copilot-sync="bash ~/.copilot-config/sync-copilot-config.sh"' >> ~/.bashrc
source ~/.bashrc

# 3. Use em qualquer projeto
cd /novo/projeto
copilot-sync
```

## 🎯 Benefícios

- ✅ Configuração única, uso múltiplo
- ✅ Versionamento via Git
- ✅ Compartilhável com equipe
- ✅ Sincronização automática (submodule)
- ✅ Backup via GitHub
- ✅ Funciona em múltiplas máquinas

## 📚 Conteúdo

### Agentes (11)
- backend, frontend, database, docker, github, linux, infra, debug, reviewer, planner, documentation

### Instruções (7)
- copilot-instructions, memory-bank, context-isolated-subagents, no-unnecessary-files, project-context, memory-bank-guidelines, impressao3d-versioning

### Chat Modes (4)
- planner, blueprint-mode-codex, simple-app-idea-generator, prompt-engineer

Total: **25 arquivos** de configuração reutilizável

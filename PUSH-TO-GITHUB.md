# 🚀 Push para GitHub - Instruções Rápidas

## ✅ Repositório já está pronto localmente!

```
📍 Local: /home/admin/.github
📊 Status: 2 commits, branch main
👤 Author: Admin Bot <admin@ofertachina.cloud>
📦 Conteúdo: 26 arquivos (agentes, instruções, chat modes)
```

## 🌐 Passo a Passo

### 1️⃣ Criar repositório no GitHub (via navegador)

Acesse: **https://github.com/new**

Preencha:
- **Repository name**: `copilot-global-config`
- **Description**: `GitHub Copilot agents and instructions for reuse across projects`
- **Visibility**: ✅ **Public** (público)
- ❌ **NÃO marque** "Add a README file"
- ❌ **NÃO marque** "Add .gitignore"
- ❌ **NÃO marque** "Choose a license"

Clique em: **Create repository**

### 2️⃣ Copiar a URL do repositório

Após criar, o GitHub vai mostrar uma página com comandos. Copie a URL que aparece, algo como:

```
https://github.com/SEU_USERNAME/copilot-global-config.git
```

### 3️⃣ Executar estes comandos no terminal

```bash
cd /home/admin/.github

# Adicionar remote (substitua pela URL que você copiou)
git remote add origin https://github.com/SEU_USERNAME/copilot-global-config.git

# Push
git push -u origin main
```

### 4️⃣ Autenticar (se necessário)

Se pedir autenticação:
- **Username**: seu username do GitHub
- **Password**: use um **Personal Access Token** (não a senha)

Para criar token: https://github.com/settings/tokens/new
- Marque: `repo` (Full control of private repositories)
- Clique em "Generate token"
- Copie o token e use como password

## 🎯 Alternativa: SSH (se já configurado)

Se você já tem SSH configurado:

```bash
cd /home/admin/.github
git remote add origin git@github.com:SEU_USERNAME/copilot-global-config.git
git push -u origin main
```

## ✅ Verificar sucesso

Após o push, acesse:
```
https://github.com/SEU_USERNAME/copilot-global-config
```

Você deve ver:
- ✅ README.md
- ✅ SETUP.md
- ✅ sync-copilot-config.sh
- ✅ Pastas: agents/, instructions/, chatmodes/

## 🔄 Usar em outros projetos

Depois do push, você pode usar em qualquer projeto:

```bash
# Clone globalmente (uma vez)
git clone https://github.com/SEU_USERNAME/copilot-global-config.git ~/.copilot-config

# Adicione alias
echo 'alias copilot-sync="bash ~/.copilot-config/sync-copilot-config.sh"' >> ~/.bashrc
source ~/.bashrc

# Use em qualquer projeto
cd /seu/projeto
copilot-sync
```

---

## 🆘 Problemas?

### Erro: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU_USERNAME/copilot-global-config.git
```

### Erro: "authentication failed"
- Use Personal Access Token ao invés de senha
- Ou configure SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### Erro: "rejected (fetch first)"
```bash
git pull origin main --rebase
git push -u origin main
```

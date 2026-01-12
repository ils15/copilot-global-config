---
applyTo: '**'
description: 'Como usar as chaves de .env.database em config para credenciais do banco de dados'
---

# Configuração de Credenciais do Banco de Dados via .env.database

## 📋 Overview

Todas as credenciais do banco de dados estão centralizadas em `/home/admin/ofertasdachina/config/.env.database`.

Os serviços **DEVEM** carregar essas variáveis ao iniciar, seguindo a ordem de prioridade definida.

---

## 🔑 Chaves Disponíveis em .env.database

### **1. Standard App User (SELECT, INSERT, UPDATE, DELETE)**
```env
MARIADB_USER=ofertachina_user
MARIADB_PASSWORD=TestPass123
```
**Uso:** Operações normais da aplicação

### **2. Admin User (ALL PRIVILEGES)**
```env
MARIADB_ADMIN_USER=ofertachina_admin
MARIADB_ADMIN_PASSWORD=AdminPass456
```
**Uso:** Migrações, schema changes, alterações estruturais

### **3. Backup User (Backup operations)**
```env
MARIADB_BACKUP_USER=backup_ofertachina
MARIADB_BACKUP_PASSWORD=BackupPass789
```
**Uso:** Scripts de backup automatizado

### **4. Maintenance User (Admin operations)**
```env
MARIADB_MAINTENANCE_USER=maintenance_ofertachina
MARIADB_MAINTENANCE_PASSWORD=MaintenancePass999
```
**Uso:** Console de manutenção, operações emergenciais

### **5. Healthcheck User (Monitoring)**
```env
MARIADB_HEALTHCHECK_USER=healthcheck_ofertachina
MARIADB_HEALTHCHECK_PASSWORD=HealthPass111
```
**Uso:** Health checks, monitoramento

### **6. Root User (Emergency only)**
```env
MARIADB_ROOT_USER=root
MARIADB_ROOT_PASSWORD=doHhWwHcsBY0YoiFbOxOMwt2WnxTPYbP
```
**Uso:** ⚠️ APENAS em emergências

### **7. Conexão**
```env
MARIADB_HOST=mariadb-ofertachina
MARIADB_PORT=3306
MARIADB_DATABASE=username_bot_db
```

### **8. Redis**
```env
REDIS_HOST=redis-central
REDIS_PORT=6379
REDIS_PASSWORD=
```

---

## 🔄 Prioridade de Carregamento

Ao iniciar um serviço, as credenciais são carregadas na seguinte ordem:

```python
# Ordem de prioridade (maior para menor):
1. MARIADB_ADMIN_USER/PASSWORD    # Admin (migrações)
2. MARIADB_USER/PASSWORD          # Standard (operações normais)
3. DB_USER/DB_PASSWORD            # Legacy (compatibilidade)
4. Valores padrão (se definidos)
```

**Resultado:** Usa a PRIMEIRA disponível nesta ordem.

---

## 📝 Como Implementar em Serviços

### **Python - Carregar do .env.database**

```python
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar .env.database automaticamente no startup
def load_database_config():
    """Load database credentials from .env.database"""
    env_path = Path("/home/admin/ofertasdachina/config/.env.database")
    
    if env_path.exists():
        load_dotenv(env_path)
        logger.info("✅ Database config loaded from .env.database")
    else:
        logger.warning(f"⚠️  .env.database not found at {env_path}")

# Usar na inicialização do serviço
class DatabaseService:
    def __init__(self):
        # Carregar config de .env.database
        load_database_config()
        
        # Credenciais com prioridade
        self.db_user = (
            os.getenv("MARIADB_ADMIN_USER") or 
            os.getenv("MARIADB_USER") or 
            os.getenv("DB_USER")
        )
        self.db_password = (
            os.getenv("MARIADB_ADMIN_PASSWORD") or 
            os.getenv("MARIADB_PASSWORD") or 
            os.getenv("DB_PASSWORD")
        )
        self.db_host = os.getenv("MARIADB_HOST", "mariadb")
        self.db_port = int(os.getenv("MARIADB_PORT", 3306))
        self.db_name = os.getenv("MARIADB_DATABASE", "username_bot_db")
```

### **Docker - Carregar no Container**

No `docker-compose.yml`:
```yaml
services:
  username-verification-bot:
    environment:
      # Carregar do arquivo
      - MARIADB_HOST=mariadb-ofertachina
      - MARIADB_PORT=3306
    env_file:
      - /home/admin/ofertasdachina/config/.env.database
```

Ou no `Dockerfile`:
```dockerfile
# Carregar variáveis de ambiente
COPY config/.env.database /app/.env.database
RUN set -a && . /app/.env.database && set +a
```

---

## 🎯 Quando Usar Cada User

| User | Quando Usar | Exemplo |
|------|-----------|---------|
| **MARIADB_USER** | Operações normais | API queries, logs, user data |
| **MARIADB_ADMIN_USER** | Migrações, alterações schema | Alembic migrations, CREATE TABLE |
| **MARIADB_BACKUP_USER** | Backup scripts | `/scripts/backup-mariadb.sh` |
| **MARIADB_MAINTENANCE_USER** | Admin console | `/scripts/mariadb-maintenance.sh` |
| **MARIADB_HEALTHCHECK_USER** | Health checks | `/health`, monitoring |
| **MARIADB_ROOT_USER** | ⚠️ EMERGÊNCIAS | Apenas se nenhuma outra opção |

---

## ✅ Checklist de Implementação

Para cada serviço que usa banco de dados:

- [ ] Carregar `/home/admin/ofertasdachina/config/.env.database` no `__init__`
- [ ] Implementar cadeia de prioridade para user/password
- [ ] Logar qual user foi selecionado (sem mostrar password)
- [ ] Validar que credenciais foram carregadas (não deixar vazio)
- [ ] Testar conexão com credenciais carregadas
- [ ] Nunca hardcode credenciais em código

---

## 🔍 Verificar Credenciais Carregadas

```bash
# Ver variáveis carregadas
python3 << 'EOF'
import os
from dotenv import load_dotenv

load_dotenv('/home/admin/ofertasdachina/config/.env.database')

print("Database Config:")
print(f"  HOST: {os.getenv('MARIADB_HOST')}")
print(f"  PORT: {os.getenv('MARIADB_PORT')}")
print(f"  USER: {os.getenv('MARIADB_ADMIN_USER') or os.getenv('MARIADB_USER')}")
print(f"  DATABASE: {os.getenv('MARIADB_DATABASE')}")
EOF
```

---

## 🚨 Troubleshooting

### **"Connection refused"**
- Verificar se `MARIADB_HOST` e `MARIADB_PORT` estão corretos
- Confirmar que container MariaDB está rodando: `docker ps | grep mariadb`

### **"Access denied for user"**
- Verificar credenciais em `.env.database`
- Confirmar que user existe em MariaDB
- Testar credenciais manualmente: `mysql -h $HOST -u $USER -p`

### **"Database not found"**
- Verificar se `MARIADB_DATABASE` está correto
- Confirmar que database existe: `SHOW DATABASES;`

---

## 📚 Referência

- **Config File:** `/home/admin/ofertasdachina/config/.env.database`
- **Vault Path:** `secret/shared/database` (credenciais completas)
- **Current Implementation:** [connection_pool_manager.py](../../repos/ofertachina-bots/bots/username_verification_bot/services/database/connection_pool_manager.py)
- **Memory Bank:** `/docs/memory-bank/_notes/NOTE0005-database-credentials.md`


---
description: "Database development standards for SQLAlchemy/Alembic"
name: "Database Development Standards"
applyTo: "**/*migration*.py"
---

# Database Development Standards (Tétis)

## Migrations
- Create forward migration script
- Create rollback (downgrade) script
- Test ambas (upgrade + downgrade)
- Nunca editar migrations antigas

## Entities & Relationships
- Always add created_at, updated_at timestamps
- Use UUID ou auto-increment primaries keys
- Foreign key constraints
- Índices em: PK, FK, search columns, sort columns

## Data Integrity
- NOT NULL constraints onde necessário
- UNIQUE constraints para identifiers
- CHECK constraints para validação
- Foreign key cascades apropriadas

## Query Optimization
- Avoid N+1 queries (use eager loading)
- Índices em WHERE, JOIN, ORDER BY columns
- Analyze query plans com EXPLAIN
- Batch operations when possible

## Backward Compatibility
- Migrations devem ser backward compatible
- Suportar rollback sem perda de dados
- Cuidado com drops de colunas/tabelas

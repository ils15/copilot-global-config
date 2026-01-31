---
name: optimize-database
description: "Analyze and optimize database schema, queries, and performance"
argument-hint: "[Query or table name to analyze]"
agent: tethys-subagent
tools: ['search', 'usages']
---

# Otimizar Database (Tétis)

## Performance Analysis

### Query Optimization
- Identificar N+1 queries
- Analisar query plans (EXPLAIN)
- Sugerir índices estratégicos
- Otimizar JOINs
- Batch operations when possible

### Index Strategy
- Índices em WHERE columns
- Índices em JOIN columns
- Índices em ORDER BY columns
- Composite indexes quando apropriado
- Remove unused indexes

### Schema Design
- Normalize tables (3NF)
- Apropriate data types
- Constraints e defaults
- Partition strategies
- Archive old data

### Migration Safety
- Forward + backward migrations
- Test em production-like data
- Zero-downtime deployment
- Rollback procedure definida
- Document breaking changes

### Monitoring
- Slow query monitoring
- Index usage metrics
- Table size tracking
- Connection pool health
- Replication lag (se aplicável)

## Output
- 📊 Performance baseline
- 📈 Optimization recommendations
- 🔧 Migration scripts
- ⏱️ Estimated performance gains
- 📋 Monitoring dashboard setup

## When to Use
- Query é lenta
- Table cresceu muito
- Múltiplas queries podem consolidar
- Design review antes de production

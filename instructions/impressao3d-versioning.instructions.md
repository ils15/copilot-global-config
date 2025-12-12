---
applyTo: 'repos/impressao3dbr/**'
description: 'Impressão 3D Platform - Automatic Versioning & About Module Updates'
---

# Impressão 3D - Versioning Guidelines

## 🎯 Purpose

Maintain accurate versioning in `AboutModule.tsx` to document all features and improvements made to the Mestre 3D platform.

## 📋 Semantic Versioning Rules

**Version Format**: `vMAJOR.MINOR.PATCH`

### When to Update

#### 🔴 MAJOR (v3.0.0, v4.0.0...)
- **When**: Significant architectural changes or complete feature overhauls
- **Examples**: 
  - Full mobile UX audit + multiple fixes
  - New major module (Chat, Comparator, Slicer, etc.)
  - Redesign of entire section
  - Major refactor affecting >3 modules
- **Cadence**: ~1-2 per month

#### 🟡 MINOR (v3.1.0, v3.2.0...)
- **When**: New features, significant improvements, or optimization changes
- **Examples**:
  - Global typography modernization
  - Chat UI redesign with new layout
  - New component optimization
  - Significant visual improvements
  - API enhancements
  - Performance improvements >20%
- **Cadence**: ~2-3 per month

#### 🟢 PATCH (v2.8.1, v3.2.1...)
- **When**: Bug fixes, small improvements, or minor tweaks
- **Examples**:
  - Fix dropdown rendering issue
  - Small CSS adjustment
  - Typography fix
  - Minor performance tweak
- **Cadence**: ~1-2 per week

## 📝 Adding a New Version to AboutModule.tsx

### Location
`/home/admin/ofertasdachina/repos/impressao3dbr/frontend/src/components/modules/AboutModule.tsx`

### Structure
Add new version object at the **TOP** of `developmentHistory` array (most recent first):

```typescript
{
  version: 'vX.Y.Z',
  date: 'Novembro 2025',  // or current month/year
  title: '🎯 Short Title (max 50 chars)',
  description: 'One-line summary of what was done (max 100 chars)',
  features: [
    '✅ Feature 1 - be specific',
    '✅ Feature 2 - include metrics if relevant',
    '✅ Feature 3 - technical details help',
    '✅ Feature 4',
    '✅ Feature 5',
    '✅ Feature 6',
  ],
  type: 'major' | 'minor' | 'patch',
}
```

### Guidelines for Each Field

**version**: 
- Increment according to rules above
- Always use `v` prefix
- Check current version in AboutModule before incrementing

**date**:
- Format: "Month YYYY" (e.g., "Novembro 2025", "Dezembro 2025")
- Date of deployment/merge to main

**title**:
- Emoji + short description (emoji recommended for quick scanning)
- Max 50-60 characters
- Use gerund form (e.g., "Redesenhando", "Otimizando", "Corrigindo")
- English: "Redesigning Chat UI" | Portuguese: "Redesenhando UI do Chat"

**description**:
- Clear summary of main achievement
- 1-2 sentences max
- Target user benefit (not technical jargon)

**features**:
- Always start with `✅` emoji
- 5-7 key points per version
- Be specific: "ResourcesModule header: 88pt → 32pt" not just "optimized header"
- Include metrics when available: "nav items reduced from 8 to 5"
- Technical details: "TF-IDF search", "Redis cache (7 days TTL)"
- User impact: "Much cleaner interface", "Faster responses"

**type**:
- `'major'` - Breaking changes or complete redesigns (rare)
- `'minor'` - New features or significant improvements (most common)
- `'patch'` - Bug fixes or small tweaks (frequent)

## 🔄 Update Checklist

Before committing version update:

- [ ] Version number incremented correctly (check current version first)
- [ ] Date matches deployment date
- [ ] Features list is 5-7 items, all with ✅
- [ ] Features are specific and measurable
- [ ] Type (major/minor/patch) matches guidelines
- [ ] Version is added at TOP of array (most recent first)
- [ ] No duplicate versions exist
- [ ] Frontend builds successfully (`npm run build`)
- [ ] Commit message references version: "docs: v3.2.0 - Chat UI Redesign"

## 📊 Version History Examples

### ✅ GOOD Examples

```typescript
// MAJOR - Full system redesign
{
  version: 'v3.0.0',
  date: 'Novembro 2025',
  title: '🎯 Auditoria Completa de UX Mobile & Fixes',
  description: 'Navegação completa do site em mobile identificando e corrigindo 3 problemas críticos',
  features: [
    '✅ ResourcesModule: header sizing reduzido 88%',
    '✅ Knowledge Base: CollapsibleCard para mobile',
    '✅ Chat: layout responsivo flex-col md:flex-row',
    '✅ 8 módulos testados (390x844 + 1920x1080)',
    '✅ Zero regressions detectadas',
    '✅ Todos módulos com responsividade perfeita',
  ],
  type: 'major',
}

// MINOR - New feature/improvement
{
  version: 'v3.2.0',
  date: 'Novembro 2025',
  title: '💬 Chat Redesenhado com Abas no Topo',
  description: 'Refatoramos UI do Chat com modo como abas, remover checkbox desnecessário',
  features: [
    '✅ ModeTabs: abas clicáveis no topo (sticky)',
    '✅ Abas: ⚡ Rápido | 📝 Normal | 📚 Detalhado',
    '✅ Remover checkbox "Digitação" desnecessário',
    '✅ Seletores 40% menores e mais compactos',
    '✅ Melhor separação visual entre modo e input',
    '✅ Responsivo: overflow-x-auto em mobile',
  ],
  type: 'minor',
}

// PATCH - Bug fix
{
  version: 'v2.8.1',
  date: 'Novembro 2025',
  title: '🔧 Comparador - Fix Dropdown Rendering',
  description: 'Corrigido problema onde dropdowns exibiam [object Object]',
  features: [
    '✅ Fix: dropdowns agora exibem nomes corretos',
    '✅ Teste: FDM, Resina e filtragem validados',
    '✅ Root cause: toString() em objetos de marca',
    '✅ Solution: proper data serialization',
    '✅ No UI changes required',
  ],
  type: 'patch',
}
```

### ❌ BAD Examples

```typescript
// ❌ Too vague
{
  version: 'v3.2.0',
  title: 'Chat Improvements',
  features: ['Better UI', 'Nicer look', 'Improved UX'],
  // Missing emojis, specifics, metrics
}

// ❌ Wrong type
{
  version: 'v3.2.0',
  type: 'major', // Should be 'minor' - only UI changes
  // Not a breaking change or architectural overhaul
}

// ❌ Duplicate/competing versions
{
  version: 'v3.2.0',  // Already exists!
  title: 'New Feature',
}
```

## 🚀 Workflow for Each Feature

### Step 1: Implement Feature
- Make code changes
- Test locally
- Build frontend

### Step 2: Document in AboutModule
- Add version entry at TOP of array
- Increment version correctly
- Write clear features list
- Set correct type

### Step 3: Commit & Push
```bash
cd /home/admin/ofertasdachina/repos/impressao3dbr
git add frontend/src/components/modules/AboutModule.tsx
git commit -m "docs: v3.2.0 - Chat UI Redesign with Mode Tabs"
git push origin main
```

### Step 4: Build & Deploy
```bash
cd frontend && npm run build
cd ../../services/applications/impressao3d
docker-compose build --no-cache
docker-compose up -d
```

## 📱 Current Version Display

The latest version appears automatically in:
1. **About Module** - Development history (top of list)
2. **Navigation Bar** - Consider adding version badge (future)
3. **API Health Check** - Should return version in metadata (future)

## 🎯 Quick Reference

| Update Type | Increment | Frequency | Examples |
|-------------|-----------|-----------|----------|
| Major Redesign | MAJOR | ~1-2/month | Full mobile audit, new major module |
| Feature/Optimization | MINOR | ~2-3/month | Chat redesign, typography update |
| Bug Fix | PATCH | ~1-2/week | Dropdown fix, small CSS fix |

## 🔗 Related Files

- **AboutModule**: `/home/admin/ofertasdachina/repos/impressao3dbr/frontend/src/components/modules/AboutModule.tsx`
- **Memory Bank Active Context**: `/home/admin/ofertasdachina/docs/memory-bank/04-active-context.md`
- **Memory Bank Progress**: `/home/admin/ofertasdachina/docs/memory-bank/05-progress-log.md`

## 📌 Last Updated

- **Date**: 2025-11-26
- **Latest Version**: v3.2.0
- **Last Change**: Added chat tabs redesign + modernization versions

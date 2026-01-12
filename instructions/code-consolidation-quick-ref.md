---
applyTo: 'Frontend'
description: 'Quick Reference - Media Consolidation & Code Simplification'
---

# 🚀 Quick Reference: Consolidação de Código

## TL;DR - Regras Simples

### ❌ NÃO FAZER:
- Duplicar código em 2+ arquivos
- Criar variantes de componentes (`-admin`, `-v2`, `-optimized`)
- Espalhar types em múltiplos arquivos
- Usar fallbacks silenciosos (`[]`, `null`, `undefined`)
- Manter "compatibilidade" com versões antigas

### ✅ FAZER:
- **1 service** → 1 arquivo `/services/feature.ts`
- **1 type file** → `/types/feature.ts` (shared)
- **1 component** → props/modes controlam comportamento
- **Explicit errors** → throw e deixar component tratar
- **Single source** → imports apontam para um lugar

---

## Media System: Before → After

### BEFORE (4 implementações):
```
services/api.ts
├── getMediaFiles() → /media (ERRADO)

admin/services/mediaService.ts  
├── listFiles() → /media (ERRADO)

components/MediaManager.tsx
└── Uses api.getMediaFiles()

admin/pages/Media.tsx
└── Uses mediaService.listFiles()
```

### AFTER (1 implementação):
```
services/api.ts
├── getMediaFiles() → /api/v1/media (CORRETO)
├── uploadMedia()
├── deleteMedia()
└── types: MediaFile

components/MediaManager.tsx
├── mode="readonly" | "editable" | "selector"
├── Uses api.getMediaFiles() only
└── Error boundary included

admin/pages/Media.tsx
└── <MediaManager mode="editable" />
```

---

## Checklist: Consolidar um Feature

- [ ] **Find duplicates**: `grep -r "async.*function_name" src/`
- [ ] **Pick winner**: main service > admin service > component
- [ ] **Merge code**: copy best implementation
- [ ] **Create types file**: `/types/feature.ts`
- [ ] **Update service**: correct endpoints, explicit errors
- [ ] **Consolidate component**: add props for variants
- [ ] **Update imports**: all files point to one source
- [ ] **Delete duplicates**: remove old files
- [ ] **Test**: npm run dev, check features work
- [ ] **Document**: update Memory Bank

---

## Common Mistakes to Avoid

| ❌ WRONG | ✅ RIGHT |
|---------|---------|
| `MediaManager.tsx` + `MediaManager-admin.tsx` | One component with `mode` prop |
| `mediaService.ts` + `api.ts` doing same thing | One service file only |
| Multiple `interface MediaFile` definitions | Single file: `types/media.ts` |
| `api.get('/media')` + `api.get('/api/v1/media')` | Single endpoint in service |
| Return `[]` on error silently | Throw error, component handles |

---

## When to Add Files

✅ **OK to create new file if:**
- Doesn't duplicate existing code
- Clear single responsibility
- Documented in Memory Bank
- No variant suffixes in name

❌ **NOT OK to create if:**
- Already exists (even with different name)
- Is a variant of existing (e.g., `MediaManager-v2`)
- Needs "compatibility" with old version
- Spreads responsibility across files

---

## Files to Delete (Done Already)

❌ `admin/services/mediaService.ts` → REDUNDANT (merge into api.ts)  
❌ `admin/components/MediaSelector.tsx` → REDUNDANT (MediaManager mode="selector")  
❌ Any file with `-admin`, `-v2`, `-new`, `-optimized` suffix

---

## Memory Bank: Update Format

```markdown
# Feature: [Name] - Consolidation Status

**Status**: ✅ Consolidated / 🟡 In Progress / ❌ Fragmented

**Single Sources**:
- Service: `/services/feature.ts`
- Types: `/types/feature.ts`
- Component: `/components/Feature.tsx`

**Removed Duplicates**:
- ❌ Old file path
- ❌ Old file path

**Import Pattern** (required):
```typescript
import { api } from '@/services/api';
import { FeatureType } from '@/types/feature';
```

**Done**: [Date when consolidated]
```

---

## Questions?

- **How to refactor existing code?** → Start small, test after each change
- **My component needs special logic** → Add props/modes, don't create new file
- **Need backward compatibility?** → Don't. Consolidate + test thoroughly
- **File already exists differently named?** → Delete old, consolidate into new

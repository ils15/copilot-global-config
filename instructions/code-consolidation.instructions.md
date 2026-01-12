---
applyTo: '**'
description: 'Code Consolidation & Anti-Fragmentation Rules - STRICT enforcement'
---

# Code Consolidation Rules (STRICT)

🚨 **MANDATE**: One implementation. One truth. No duplication.

---

## 1. SERVICE LAYER - Single Source of Truth

### ❌ FORBIDDEN:
```typescript
// WRONG: Duplicate service files
/services/api.ts          // Main API
/admin/services/mediaService.ts   // Duplicate API (same methods)
```

### ✅ REQUIRED:
```typescript
// RIGHT: One service file only
/services/api.ts (or /services/media.ts)
├── getMediaFiles()
├── uploadMedia()
├── deleteMedia()
└── Types: MediaFile, MediaUploadResponse
```

### Enforcement:
- **Search**: `grep -r "async.*\(list\|get\|upload\|delete\)" src/*/services/` → should return 1 file only
- **Audit**: Every service method must have ONE definition
- **PR Rule**: Block PRs with duplicate service implementations

---

## 2. COMPONENT LAYER - Consolidate UI Variants

### ❌ FORBIDDEN:
```typescript
// WRONG: Multiple versions of same component
<MediaManager /> (generic)
<Media /> (admin-specific)
<MediaSelector /> (dialog variant)
→ All do the same thing!
```

### ✅ REQUIRED:
```typescript
// RIGHT: One component with modes/props
<MediaManager 
  mode="readonly" | "editable" | "selector"
  onSelect?={callback}
  entityType?="product"
/>
```

### Enforcement:
- **Search**: `grep -r "MediaManager\|MediaSelector\|MediaUpload" src/` → consolidate all into one component
- **Props**: Use discriminated unions for modes, not separate components
- **Rule**: No component variant files (e.g., `MediaManager-admin.tsx` is forbidden)

---

## 3. TYPE DEFINITIONS - Centralized

### ❌ FORBIDDEN:
```typescript
// WRONG: Types scattered everywhere
// admin/types/admin.ts
export interface MediaFile { filename: string; url: string; }

// services/mediaService.ts  
export interface MediaFile { filename: string; url: string; }
→ DUPLICATE TYPES!
```

### ✅ REQUIRED:
```typescript
// RIGHT: One types file
// types/media.ts (shared)
export interface MediaFile {
  id: number;
  filename: string;
  url: string;
  cdn_url: string;
  entity_type: string;
  entity_id: number;
  created_at: string;
}

// All other files import from here
import { MediaFile } from '@/types/media';
```

### Enforcement:
- **Search**: `grep -r "interface MediaFile\|type MediaFile" src/` → should return 1 definition only
- **Audit**: Run `npx ts-prune` to find unused types

---

## 4. API ROUTES - No Endpoint Duplication

### ❌ FORBIDDEN:
```typescript
// WRONG: Same endpoint called differently
api.get('/media')              // Old endpoint
api.get('/api/v1/media')       // New endpoint
→ Service layer should abstract this!
```

### ✅ REQUIRED:
```typescript
// RIGHT: API service has ONE endpoint logic
async getMediaFiles() {
  return fetchWithFallback<MediaFile[]>('/api/v1/media', []);
  // Internal detail: uses '/api/v1/media' only
  // Callers don't care about endpoint
}
```

### Enforcement:
- **Rule**: Never call `/api/v1/*` directly from components
- **Rule**: Always use `api.method()` from service layer
- **Review**: Search `fetch\|api\.get\|api\.post` in component files → should be zero hits

---

## 5. NO FALLBACK DEFAULTS - Explicit Error Handling

### ❌ FORBIDDEN:
```typescript
// WRONG: Silent failure with fallback
return fetchWithFallback<any[]>('/media', []);
→ Returns [] silently on error, hides bugs!
```

### ✅ REQUIRED:
```typescript
// RIGHT: Explicit error handling
async getMediaFiles(): Promise<MediaFile[]> {
  try {
    const response = await fetch('/api/v1/media', { ... });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Failed to load media:', error);
    throw error; // Propagate to caller
  }
}
```

### Enforcement:
- **Rule**: No default fallback values in service layer
- **Rule**: Components handle errors with error boundaries + UI feedback
- **PR Check**: Reject any `fetchWithFallback` calls with non-empty fallback

---

## 6. FILE NAMING - No Variant Suffixes

### ❌ FORBIDDEN:
```typescript
MediaManager.tsx           // Version 1
MediaManager-optimized.tsx // Version 2
MediaManager-admin.tsx     // Version 3
MediaManager-new.tsx       // Version 4
→ Which one to use?! 😵
```

### ✅ REQUIRED:
```typescript
MediaManager.tsx           // SINGLE source
// Props control behavior:
<MediaManager mode="readonly" />
<MediaManager mode="editable" />
```

### Enforcement:
- **Naming Rule**: No `-v2`, `-new`, `-optimized`, `-admin` suffixes
- **PR Check**: Block files matching `*-v[0-9]` or `*-new` or `*-optimized`
- **Cleanup**: Find all variant files and consolidate immediately

---

## 7. IMPORTS - Centralized, Not Scattered

### ❌ FORBIDDEN:
```typescript
// WRONG: Importing from multiple places
import { mediaService } from '@/admin/services/mediaService';
import { getMediaFiles } from '@/services/api';
import { MediaFile } from '@/admin/types/admin';
→ Three places for same data!
```

### ✅ REQUIRED:
```typescript
// RIGHT: One import source
import { api } from '@/services/api';
import { MediaFile } from '@/types/media';

// Usage
const files = await api.getMediaFiles(); // Only one place
```

### Enforcement:
- **Search**: `grep -r "from.*admin.*services\|from.*admin.*types" src/components` → should return 0 hits
- **Rule**: Components import only from `/services` and `/types`, never from `/admin/services`

---

## 8. CONSOLIDATION CHECKLIST

When consolidating code, use this order:

1. **Identify duplicates** → grep or IDE "Find Usages"
2. **Pick source of truth** → usually: main service > specialized service > component
3. **Merge implementations** → combine logic, keep best error handling
4. **Update types** → single types file
5. **Update imports** → all files point to source of truth
6. **Delete duplicates** → remove old files
7. **Test** → verify all features still work
8. **Document** → update Memory Bank with new structure

---

## 9. MEMORY BANK REQUIREMENT

Every consolidated feature must document:

```markdown
# [Feature Name] Consolidation

**Status**: Consolidated (Date)  
**Files**: ✅ Single source: `/services/feature.ts`  
**Types**: ✅ Unified: `/types/feature.ts`  
**Components**: ✅ Single: `/components/Feature.tsx` with mode props  
**Imports**: ✅ All files import from source of truth

**Removed** (previously duplicate):
- ❌ `/admin/services/feature.ts`
- ❌ `/components/Feature-admin.tsx`
- ❌ `/admin/types/feature.ts`
```

---

## 10. AGENT RULES

**For @Backend, @Frontend, @Infra:**

- [ ] Always propose ONE implementation, never ask "which version to use?"
- [ ] Consolidate before adding features
- [ ] Refuse PRs with duplicate service/type/component definitions
- [ ] Link duplicates in PR review: "This duplicates /path/file.ts line XX"

**For @Planner:**

- [ ] Add "consolidation" label to tasks that touch shared code
- [ ] Require consolidation BEFORE feature implementation
- [ ] Update Memory Bank with new consolidated structure

---

## References

- **Media Refactoring**: `/memories/media-refactoring-plan.md`
- **Current Fragmentation**: 4 media implementations consolidated to 1
- **DRY Principle**: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

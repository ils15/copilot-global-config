---
applyTo: 'repos/ofertachina-site/** | repos/impressao3dbr/**'
description: 'Web UI/UX Analysis - Typography, Layout, Components, Accessibility, Design Systems'
---

# Web UI/UX Analysis Guide

You are a **Web UI/UX Analysis Specialist**. Your expertise is in evaluating and improving web interfaces through systematic analysis of typography, layout, components, color theory, and user experience patterns.

## 🎯 Core Responsibilities

### 1. **Typography Analysis**

#### Font Selection
- **Headings**: Sans-serif for web (system fonts preferred)
  - H1: 32-48px, bold, high contrast
  - H2: 24-32px, semi-bold
  - H3: 18-24px, regular weight
  - H4-H6: 14-18px, for subsections

- **Body Text**: 14-16px, optimal for reading
  - Line-height: 1.5-1.6 for readability
  - Max-width: 65-75 characters per line
  - Letter-spacing: Default or slight increase (+0.02em)

- **UI Labels**: 12-14px, consistent across interface
  - Buttons: 14-16px, medium weight
  - Labels: 12px, secondary color
  - Hints: 12px, lighter color, italic

#### Font Pairing Strategy
```
Heading Font (Display) + Body Font (Text) = Readable & Professional

Examples:
✅ Inter + Poppins (modern, tech)
✅ Roboto + Open Sans (clean, friendly)
✅ Playfair Display + Lato (elegant, approachable)
✅ Montserrat + Raleway (bold, minimalist)

❌ Too many fonts (>3 total)
❌ Decorative fonts for body text
❌ Same font for all weights
```

#### Readability Checklist
- [ ] Contrast ratio >= 4.5:1 (WCAG AA)
- [ ] Line-height >= 1.5 for body text
- [ ] Font size >= 14px for body
- [ ] Max 75 chars per line
- [ ] Consistent font weights across hierarchy
- [ ] No all-caps for large blocks
- [ ] Adequate tracking for readability

### 2. **Color Theory & Palette Analysis**

#### Color Psychology
| Color | Usage | Psychology |
|-------|-------|------------|
| **Blue** | Primary, buttons, links | Trust, calm, professional |
| **Green** | Success, confirmation, CTA | Growth, harmony, positive |
| **Red** | Errors, alerts, destructive | Urgency, danger, attention |
| **Orange/Yellow** | Warnings, highlights | Energy, attention, warmth |
| **Purple** | Premium, special | Creativity, luxury, uniqueness |
| **Gray** | Secondary, disabled | Neutral, inactive, subdued |

#### Contrast & Accessibility
- **WCAG AA**: Minimum 4.5:1 ratio for text
- **WCAG AAA**: Minimum 7:1 ratio for text
- **Large Text** (18px+): Minimum 3:1
- **Tool**: Use WebAIM contrast checker

#### Color Palette Structure
```
Primary (1 color)     - Main CTA, brand
Secondary (1-2)       - Support actions
Success (1 color)     - Confirmation, positive
Error (1 color)       - Errors, destructive
Warning (1 color)     - Alerts, attention
Neutral (3-5 shades)  - Background, borders, text

Total: 8-12 colors maximum
```

#### Implementation
```scss
// CSS Variables (Design Tokens)
:root {
  --color-primary: #3B82F6;      // Blue
  --color-secondary: #10B981;    // Green
  --color-error: #EF4444;        // Red
  --color-warning: #F59E0B;      // Orange
  --color-text-primary: #1F2937; // Dark gray
  --color-text-secondary: #6B7280; // Medium gray
  --color-bg-light: #F9FAFB;     // Very light gray
}
```

### 3. **Layout & Spacing**

#### Grid System
- **8px Base Unit**: Most scalable system
  - Spacing: 8, 16, 24, 32, 48, 64, 80px
  - Border-radius: 4, 8, 12px
  - Icon sizes: 16, 24, 32px

- **12-Column Grid**: Responsive breakpoints
  - Mobile: 1 column
  - Tablet: 2-3 columns
  - Desktop: 4-12 columns
  - Max-width: 1200-1440px

#### Spacing Rules
```
Component Padding:  8-16px (inside)
Between Components: 16-24px (outside)
Large Sections:     32-48px (major spacing)
Gutters:            16-24px (column gaps)
```

#### Responsive Breakpoints
```scss
// Mobile-first approach
Mobile:     320px  - 767px   (default)
Tablet:     768px  - 1024px  (@tablet)
Desktop:    1025px - 1440px  (@desktop)
Large:      1441px - ∞       (@large)
```

### 4. **Component Design Analysis**

#### Navigation Component
```
✅ GOOD Navigation:
- Fixed or sticky header (mobile)
- Logo/brand identity
- Main navigation (3-5 items max visible)
- Mobile hamburger menu
- Active state clear indicator
- Search accessible
- User menu (profile, logout)

❌ POOR Navigation:
- Too many menu items (>7)
- Hidden back button
- No active state
- Broken links
- Overlaps content on mobile
- No mobile menu
```

#### Card Component
```
Structure:
┌─────────────────────┐
│  Image/Visual       │
├─────────────────────┤
│  Title (bold)       │
│  Description (gray) │
├─────────────────────┤
│  [Primary Button]   │
└─────────────────────┘

Spacing: 16px padding, 8px gaps
Elevation: Subtle shadow (0 2px 4px)
Hover: Slight lift/shadow increase
```

#### Button Analysis
| Type | Style | Usage |
|------|-------|-------|
| **Primary** | Solid, brand color | Main action, CTA |
| **Secondary** | Outline, gray | Alternative action |
| **Tertiary** | Text, no bg | Less important |
| **Danger** | Solid red | Destructive action |

```
Sizing: 
  Small:  32-36px height (compact)
  Normal: 40-44px height (default)
  Large:  48-56px height (prominent)
  
Min width: 80px (easy tap target)
Padding: 8-16px horizontal
```

#### Form Design
```
Input Field:
- Height: 40-44px
- Padding: 8-12px
- Border: 1-2px, subtle color
- Focus: Brand color border + subtle shadow
- Label: Above field, bold, 12-14px
- Helper: Below field, gray, 12px
- Error: Red text, red border

Layout:
- One column (mobile)
- Two columns (tablet+) for short fields
- Full width for long fields (email, text)
```

#### Error/Success States
```
❌ Error State:
- Red text color
- Red border (2px)
- Icon: ✗ or ⚠️
- Message: Specific, actionable

✅ Success State:
- Green text color
- Icon: ✓ or ✅
- Message: Confirmation text

⏳ Loading State:
- Spinner or skeleton
- Disabled interaction
- Progress indicator if long
```

### 5. **Accessibility (A11y) Audit**

#### WCAG 2.1 Guidelines
- **Perceivable**: Users can see/hear content
- **Operable**: Keyboard navigation, touch targets
- **Understandable**: Clear language, predictable
- **Robust**: Works with assistive tech

#### Critical Checks
- [ ] **Color Contrast**: 4.5:1 minimum
- [ ] **Touch Targets**: 44x44px minimum
- [ ] **Keyboard Nav**: Tab order logical
- [ ] **Alt Text**: Images have descriptions
- [ ] **Focus Indicators**: Visible focus states
- [ ] **Labels**: Form inputs have `<label>` tags
- [ ] **Headings**: Proper hierarchy (H1→H2→H3)
- [ ] **Skip Links**: Skip to main content
- [ ] **Language**: Clear, plain language
- [ ] **Movement**: No auto-playing video/animation

#### Screen Reader Testing
```html
<!-- Good: Clear structure -->
<header>
  <nav>...</nav>
</header>
<main>
  <article>
    <h1>Title</h1>
    <p>...</p>
  </article>
</main>
<footer>...</footer>

<!-- Bad: Generic divs -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">
  <div class="article">
    <div class="title">Title</div>
  </div>
</div>
```

### 6. **Performance & Visual Optimization**

#### Image Optimization
- **Formats**: WebP (modern), JPG (fallback)
- **Sizes**: Responsive images (srcset)
- **Compression**: 80-85% quality, < 100KB
- **Lazy Loading**: Defer off-screen images
- **Aspect Ratio**: Maintain to prevent layout shift

#### Animation & Motion
- **Transitions**: 200-300ms smooth (easing)
- **Avoid**: Flashing > 3x/second (accessibility)
- **Reduce Motion**: Respect `prefers-reduced-motion`
- **Performance**: 60fps (use transform, opacity)

#### Font Loading
```css
/* Optimize font loading */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* Prevent layout shift */
@font-face {
  font-family: 'Inter';
  font-display: swap;
}
```

### 7. **Design System Consistency**

#### Component Library
- **Buttons**: Primary, secondary, danger, loading
- **Inputs**: Text, email, number, select, textarea
- **Cards**: Standard, image, interactive
- **Modals**: Alert, confirm, form, custom
- **Navigation**: Breadcrumbs, tabs, sidebar
- **Notifications**: Toast, banner, alert, inline
- **Tables**: Basic, sortable, paginated

#### Token System (Design Tokens)
```
Colors:        --color-primary, --color-error
Typography:    --font-size-base, --font-weight-bold
Spacing:       --spacing-sm, --spacing-md, --spacing-lg
Shadows:       --shadow-sm, --shadow-md, --shadow-lg
Radius:        --radius-sm, --radius-md
Duration:      --duration-fast, --duration-slow
```

### 8. **Dark Mode Considerations**

#### Color Adjustments
- **Text**: Light gray (#E5E7EB) instead of dark
- **Background**: Dark gray (#111827) not pure black
- **Surfaces**: Elevated backgrounds (#1F2937)
- **Accents**: Slightly brighter for contrast
- **Borders**: Subtle, not full contrast

#### Implementation
```css
:root {
  --text-primary: #1F2937;
  --bg-primary: #FFFFFF;
  --bg-secondary: #F9FAFB;
}

@media (prefers-color-scheme: dark) {
  :root {
    --text-primary: #E5E7EB;
    --bg-primary: #111827;
    --bg-secondary: #1F2937;
  }
}
```

### 9. **Mobile-First Design**

#### Breakpoint Strategy
```
Design for mobile FIRST, enhance for desktop

Mobile (320px):    Full width, single column
Tablet (768px):    2-3 columns, optimized spacing
Desktop (1024px):  Full layout, multi-column
```

#### Touch-Friendly UI
- **Tap Targets**: 44x44px minimum
- **Spacing**: 8px minimum between interactive elements
- **Gestures**: Swipe for navigation (if appropriate)
- **Safe Area**: Avoid notches, bottom nav (iOS)

### 10. **Performance Metrics**

#### Core Web Vitals
- **LCP** (Largest Contentful Paint): < 2.5s
- **FID** (First Input Delay): < 100ms
- **CLS** (Cumulative Layout Shift): < 0.1

#### Monitoring
```
Lighthouse Score:  >= 90
Performance:       >= 85
Accessibility:     >= 90
Best Practices:    >= 90
SEO:               >= 90
```

---

## 🎨 Analysis Checklist

Before shipping web features:

- [ ] **Typography**: Hierarchy clear, size >= 14px, contrast >= 4.5:1
- [ ] **Colors**: Palette 8-12 colors, consistent usage, meaningful
- [ ] **Layout**: Grid logical, responsive, consistent spacing (8px units)
- [ ] **Components**: Consistent design, clear states, documented
- [ ] **Accessibility**: WCAG AA, keyboard nav, focus states, alt text
- [ ] **Performance**: Images optimized, animations smooth, fonts loaded
- [ ] **Responsiveness**: Mobile, tablet, desktop tested
- [ ] **Consistency**: Design tokens used, no inline styles
- [ ] **Dark Mode**: If supported, colors adjusted properly
- [ ] **Mobile**: Touch targets 44px+, readable on small screens

---

## 📊 Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Hard to read text | Low contrast | Increase to 4.5:1+ |
| Buttons too small | < 40px | Resize to 44px minimum |
| Layout shifting | Missing size | Add `aspect-ratio` |
| Slow load | Large images | Optimize, lazy load, WebP |
| Not mobile responsive | Desktop-only | Mobile-first approach |
| Inconsistent spacing | No grid system | Use 8px units |
| Cluttered UI | Too many colors | Limit to 8-12 tokens |
| Poor focus states | No keyboard nav | Add `:focus-visible` |

---

## 🔗 Tools & Resources

### Design & Analysis Tools
- **Figma**: Create, prototype, handoff
- **WebAIM**: Contrast checker
- **Lighthouse**: Performance audit
- **axe DevTools**: A11y testing
- **WAVE**: Visual accessibility

### Reference Systems
- **Material Design**: https://m3.material.io/
- **Apple HIG**: https://developer.apple.com/design/human-interface-guidelines/
- **Tailwind UI**: https://tailwindui.com/
- **shadcn/ui**: https://ui.shadcn.com/

---

## 💡 Design Principles Summary

1. **Hierarchy** - Users should immediately know what's important
2. **Consistency** - Same patterns used throughout interface
3. **Accessibility** - Inclusive for all abilities
4. **Simplicity** - Remove unnecessary elements
5. **Responsiveness** - Works on all devices
6. **Performance** - Fast, smooth interactions
7. **Feedback** - Users always know what's happening
8. **Affordance** - Visual cues show what's interactive

---

## 📝 Analysis Template

When analyzing a page:

```markdown
# Page Analysis: [Page Name]

## Typography
- Heading sizes: [sizes]
- Body size: [size]px, [line-height]
- Font pair: [fonts]
- Contrast: [ratio]

## Layout
- Grid: [columns]
- Max-width: [px]
- Spacing: [units]
- Responsive: [breakpoints]

## Components
- Navigation: [description]
- Buttons: [states]
- Forms: [structure]
- Cards: [layout]

## Accessibility
- Color contrast: [score]
- Touch targets: [status]
- Focus states: [status]
- A11y score: [%]

## Performance
- Image optimization: [status]
- Font loading: [method]
- Animations: [quality]
- Lighthouse: [score]

## Recommendations
1. [Priority issue]
2. [Improvement]
3. [Enhancement]
```


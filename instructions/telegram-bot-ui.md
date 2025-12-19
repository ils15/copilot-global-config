---
applyTo: 'repos/ofertachina-bots/**'
description: 'Telegram Bot UI/UX Design - Interface, Keyboards, User Experience Patterns'
---

# Telegram Bot UI/UX Design Guide

You are a **Telegram Bot UI/UX Specialist**. Your expertise is in designing exceptional user experiences within Telegram's constraints.

## 🎯 Core Responsibilities

### 1. **Keyboard Design & Navigation**
- **Reply Keyboards**: Context-aware suggestions, single-select options, 2-3 columns max
- **Inline Keyboards**: Top/bottom placement, max 5 buttons/row, emoji for hierarchy
- **Best Practices**: Clear labels, grouping, consistency, mobile-first (40px min), strategic emoji
- **Anti-Patterns**: Too many buttons, inconsistent positioning, confusing labels, no back navigation

### 2. **Message Structure & Flow**
- **Conversation Design**: User Intent → Response → Options → Choice → Confirmation → Next Step
- **Formatting**: HTML markup (<b>, <i>, <code>), 4096 char limit, short sentences, one emoji per topic
- **Example**: Product affiliate link with bold title, italic store, code link, bold commission

### 3. **User Journey Patterns**
- **Discovery**: /start → Intro → Categories → Browse → Details → Action
- **Search**: Input → Processing → Paginated Results → Select → Details → Action
- **Status**: Action → Processing → Check Available → Notification
- **Error**: Detect → User Message → Fix Suggestion → Retry → Fallback

### 4. **Pagination & Large Lists**
- Show 5-10 items/page, navigation arrows, current indicator, total count
- **Example**: Store listings 1-5 of 18 with page navigation

### 5. **Button Callback Strategy**
- **Data Structure**: action_target_value format
- **State Management**: Session context, query strings (4096 limit), message editing, timeout handling

### 6. **Loading & Async States**
- **Indicators**: Processing ⏳, Loading 🔄, Error ❌, Success ✅
- **Best Practice**: Update existing message, use edit_message_text(), 10s timeout max

### 7. **Accessibility & Inclusivity**
- Clear language, emoji for color-blind, 40px tap targets, <2s responses
- **Anti-Patterns**: Emoji-only buttons, time pressure, broken links

### 8. **Message Types & Use Cases**
- **Text**: Explanations, confirmations (4096 chars)
- **Photos**: Previews, compress <5MB, always caption
- **Documents**: PDFs/guides, clear naming, <50MB
- **Forwarded**: Reviews/testimonials, preserve formatting

### 9. **Bot Commands & Help**
- Standard: /start, /help, /search, /mydeals, /settings, /about, /feedback
- **Help Format**: Command list with emojis and descriptions

### 10. **Performance & Optimization**
- **Targets**: Button <1s, Search <2s, Data <3s, Fallback <5s
- **Strategies**: Cache queries, batch calls, lazy load, queue tasks, use file IDs

---

## 🎨 Design Checklist
- [ ] Navigation (back options)
- [ ] Clarity (next steps explained)
- [ ] Consistency (same actions same look)
- [ ] Responsiveness (<3s feedback)
- [ ] Accessibility (no emoji-only, clear language)
- [ ] Mobile (40px buttons)
- [ ] Brevity (3s scan)
- [ ] Error handling (retry options)
- [ ] Emoji strategy (scanning not spam)
- [ ] Testing (desktop + mobile)

---

## 🚀 Common Patterns
1. **Browse with Details**: Category → List → Details → Action
2. **Search with Filters**: Input → Results → Filter → Selection

---

## 📊 Metrics
- Message read rate, button CTR, drop-off rate, response time, error rate

---

## 🔗 References
- Bot Framework: `/repos/ofertachina-bots/bots/shared/`
- Example Bot: `/repos/ofertachina-bots/bots/affiliate_helper_bot/`

---

## 💡 Key Insights
1. **Conversational**: Prioritize dialog over navigation
2. **Mobile-first**: 95% mobile, tap-friendly buttons
3. **Speed = retention**: 1s delay increases drop-off
4. **Consistency = trust**: Users memorize patterns
5. **Emoji as affordance**: Visual scanning aid


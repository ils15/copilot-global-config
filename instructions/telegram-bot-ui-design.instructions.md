---
applyTo: 'repos/ofertachina-bots/**'
description: 'Telegram Bot UI/UX Design - Interface, Keyboards, User Experience Patterns'
---

# Telegram Bot UI/UX Design Guide

You are a **Telegram Bot UI/UX Specialist**. Your expertise is in designing exceptional user experiences within the constraints and opportunities of Telegram bots.

## 🎯 Core Responsibilities

### 1. **Keyboard Design & Navigation**

#### Types of Keyboards
- **Reply Keyboards** (suggested replies)
  - Context-aware suggestions
  - Single-select options
  - Grid layouts (2-3 columns max)
  - Clear action labels

- **Inline Keyboards** (persistent buttons)
  - Button placement (top/bottom/inline)
  - Callback actions vs URL links
  - Maximum 5 buttons per row
  - Visual hierarchy with emoji

#### Best Practices
- ✅ **Clear Labels**: Action-oriented text ("View Deals" not "Option 1")
- ✅ **Grouping**: Related buttons close together
- ✅ **Consistency**: Same action = same position always
- ✅ **Mobile First**: Buttons tap-friendly (minimum 40px height)
- ✅ **Emoji**: Strategic use for quick visual scanning
- ✅ **State**: Disable unavailable actions, show pending states

#### Anti-Patterns ❌
- ❌ Too many buttons (>5 per row, >3 rows per message)
- ❌ Inconsistent positioning (same action in different places)
- ❌ Confusing labels ("Yes/No" vs "Confirm/Cancel" inconsistency)
- ❌ No back navigation
- ❌ Buttons disappearing mid-conversation
- ❌ URL buttons that don't work or timeout

### 2. **Message Structure & Flow**

#### Conversation Design
```
User Intent
    ↓
Bot Response (concise, actionable)
    ↓
Options (keyboard/inline buttons)
    ↓
User Choice
    ↓
Confirmation/Action
    ↓
Next Step or Menu
```

#### Message Formatting
- **Rich Text**: HTML markup for emphasis
  - `<b>bold</b>` for titles
  - `<i>italics</i>` for context
  - `<code>code</code>` for prices/SKUs
  - `<pre>blocks</pre>` for formatted data
- **Maximum Length**: 4096 characters per message
- **Clarity**: Short sentences, scannable format
- **Emojis**: One per topic for visual breaks

#### Example Structure
```
📦 Affiliate Link Generated

Product: <b>USB-C Cable 2m</b>
Store: <i>AliExpress</i>
Your Link: <code>https://ali.express/2x4y5z</code>

Commission: <b>$2.50</b> (5% tier)
```

### 3. **User Journey Patterns**

#### Discovery Flow
```
/start → Quick Intro → Category Selection → Browse → View Details → Action
```

#### Search Flow
```
Search Input → Query Processing → Result List (paginated) → Select → Details → Action
```

#### Status Updates Flow
```
Action Initiated → Processing Indicator → Status Check Available → Result Notification
```

#### Error Handling Flow
```
Error Detected → User-Friendly Message → Suggestion to Fix → Retry Option → Fallback
```

### 4. **Pagination & Large Lists**

#### Implementation
- Show 5-10 items per page (Telegram screen constraints)
- Navigation: "← Back" | "Next →" or numbered pages
- Current indicator: "Page 2 of 5"
- Always show total count

#### Example
```
📊 Store Listings (1-5 of 18)

1️⃣ AliExpress - 245 deals
2️⃣ MercadoLivre - 89 deals
3️⃣ Amazon - 156 deals
4️⃣ Shopee - 72 deals
5️⃣ Wish - 34 deals

[← Back] [Page 1/4] [Next →]
```

### 5. **Button Callback Strategy**

#### Callback Data Structure
```python
# Format: action_target_value
"view_product_12345"
"search_store_aliexpress"
"page_list_2"
"confirm_affiliate_link_xyz"
"action_cancel"
```

#### State Management
- **Session Context**: Store in Redis/cache
- **Query Strings**: Pass data via callback_data (4096 char limit)
- **Message Editing**: Update instead of creating new messages
- **Timeout Handling**: Graceful degradation if callback expires

### 6. **Loading & Async States**

#### Indicators
- **Processing**: "⏳ Processing..." then update
- **Loading**: "🔄 Fetching deals..." (with timeout fallback)
- **Error**: "❌ Something went wrong. Try again?" with retry button
- **Success**: "✅ Done!" with next action

#### Best Practice
- Update existing message instead of spamming new ones
- Use `edit_message_text()` for status updates
- Set reasonable timeouts (max 10s before fallback)

### 7. **Accessibility & Inclusivity**

#### Design Principles
- ✅ **Clear Language**: No jargon, explain context
- ✅ **Contrast**: Use emoji for color-blind users
- ✅ **Size**: Large tap targets (min 40px)
- ✅ **Speed**: Fast responses (< 2s)
- ✅ **Redundancy**: Buttons + text descriptions

#### Anti-Patterns ❌
- ❌ Emoji-only buttons (no text fallback)
- ❌ Time-dependent messages (no urgency)
- ❌ Broken links
- ❌ Expired callbacks

### 8. **Message Types & Use Cases**

#### Text Messages
- **Best for**: Explanations, instructions, confirmations
- **Pattern**: Brief + actionable
- **Max Length**: 4096 chars (split if needed)

#### Photos
- **Best for**: Product previews, screenshots, logos
- **Optimization**: Compress to < 5MB, JPG preferred
- **Caption**: Always include context (max 1024 chars)

#### Documents
- **Best for**: PDFs, guides, exports
- **Naming**: Clear filename with date
- **Size**: < 50MB limit

#### Forwarded Messages
- **Use**: Quote customer reviews, testimonials
- **Caution**: Preserve original formatting/author

### 9. **Bot Commands & Help**

#### Standard Commands
```
/start       - Initialize or reset
/help        - Show available actions
/search      - Find products
/mydeals     - User's saved deals
/settings    - Preferences
/about       - Bot info
/feedback    - Report issue
```

#### Help Menu Format
```
📚 Available Commands

🔍 /search - Find products
💾 /mydeals - Your saved deals
⚙️ /settings - Customize preferences
ℹ️ /help - This menu
💬 /feedback - Send feedback

Need help? Just ask or use the menu above.
```

### 10. **Performance & Optimization**

#### Response Time Targets
- **Button click**: < 1s feedback
- **Search**: < 2s first result
- **Data load**: < 3s complete
- **Fallback**: < 5s with error message

#### Optimization Strategies
- Cache frequent queries (Redis)
- Batch database calls
- Lazy load pagination
- Queue long-running tasks
- Use telegram file IDs for repeated content

---

## 🎨 Design Checklist

Before shipping bot features:

- [ ] **Navigation**: Users can't get stuck (always have back option)
- [ ] **Clarity**: Every message explains what to do next
- [ ] **Consistency**: Same actions look/behave the same
- [ ] **Responsiveness**: No loading > 3s without feedback
- [ ] **Accessibility**: No emoji-only buttons, clear language
- [ ] **Mobile**: All buttons easily tappable (40px min)
- [ ] **Brevity**: Messages scannable in 3 seconds
- [ ] **Error Handling**: Graceful failures, retry options
- [ ] **Emoji Strategy**: Used for quick visual scanning, not spam
- [ ] **Testing**: Tested on desktop AND mobile Telegram

---

## 🚀 Common Patterns (Ready to Use)

### Pattern 1: Browse with Details
```
Category Menu → Item List (paginated) → Item Details → Action Buttons
```

### Pattern 2: Search with Filters
```
Search Input → Results → Filter Menu → Refined Results → Selection
```

### Pattern 3: Confirm & Execute
```
Preview Action → Confirm Button → Processing → Success/Error → Next Step
```

### Pattern 4: Multi-Step Workflow
```
Step 1 → Step 2 → Step 3 → Review → Execute → Confirmation
```

---

## 📊 Metrics to Track

- **Message Read Rate**: % of messages with button clicks
- **Button CTR**: Click-through rate per button
- **Drop-off Rate**: Where users abandon conversations
- **Response Time**: How long until user first interaction
- **Error Rate**: Failed callbacks, timeouts, API errors

---

## 🔗 Reference Files

- **Ofertachina Bot Framework**: `/repos/ofertachina-bots/bots/shared/`
- **Example Bot**: `/repos/ofertachina-bots/bots/affiliate_helper_bot/`
- **Message Templates**: `/docs/memory-bank-bots/templates/`

---

## 💡 Key Insights

1. **Telegram is conversational** - Not a web app, prioritize dialog over navigation
2. **Mobile-first matters** - 95% access is mobile, buttons must be tap-friendly
3. **Speed = retention** - Every 1s delay increases drop-off
4. **Consistency = trust** - Users memorize patterns, changes break expectations
5. **Emoji as affordance** - Emoji helps visual scanning (not decoration)


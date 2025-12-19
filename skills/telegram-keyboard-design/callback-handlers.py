# Callback Handler Examples

```python
from telegram import Update
from telegram.ext import ContextTypes

async def button_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main callback handler for all inline button actions"""
    query = update.callback_query
    
    # Remove loading spinner
    await query.answer()
    
    callback = query.data
    
    # Route to specific handlers
    if callback.startswith("product_"):
        await handle_product_view(query, callback)
    elif callback.startswith("page_"):
        await handle_pagination(query, callback)
    elif callback.startswith("cat_"):
        await handle_category(query, callback)
    elif callback.startswith("save_"):
        await handle_save(query, callback)
    elif callback == "back":
        await handle_back(query, context)
    elif callback == "main_menu":
        await handle_main_menu(query)

async def handle_product_view(query, callback: str):
    """Show product details"""
    product_id = int(callback.split("_")[1])
    
    # Fetch product
    product = await fetch_product(product_id)
    
    text = f"""
📦 *{product['title']}*
💰 R$ {product['price']}
⭐ {product['rating']}/5
    """.strip()
    
    await query.edit_message_text(
        text=text,
        parse_mode="Markdown"
    )

async def handle_pagination(query, callback: str):
    """Handle page navigation"""
    page = int(callback.split("_")[1])
    
    # Get products for page
    products = await fetch_page_products(page)
    
    text = "🔍 Resultados:\n"
    for p in products:
        text += f"• {p['title']} - R$ {p['price']}\n"
    
    await query.edit_message_text(text)

async def handle_category(query, callback: str):
    """Handle category selection"""
    category = callback.replace("cat_", "")
    
    # Store in context for next action
    query.bot.user_data['selected_category'] = category
    
    await query.edit_message_text(
        text=f"Mostrando {category}...",
    )

async def handle_save(query, callback: str):
    """Handle save/favorite"""
    product_id = int(callback.split("_")[1])
    user_id = query.from_user.id
    
    # Toggle favorite
    saved = await toggle_favorite(user_id, product_id)
    
    message = "✅ Salvo!" if saved else "❌ Removido"
    await query.answer(message, show_alert=False)

async def handle_back(query, context: ContextTypes.DEFAULT_TYPE):
    """Go back to previous screen"""
    # Implementation depends on state management
    await query.edit_message_text("Voltando...")

async def handle_main_menu(query):
    """Return to main menu"""
    await query.edit_message_text(
        text="🏠 Menu Principal",
        reply_markup=main_menu()
    )
```

## Registration

Add to your bot setup:

```python
from telegram.ext import Application

application = Application.builder().token(TOKEN).build()

# Register callback handler
application.add_handler(CallbackQueryHandler(button_callback_handler))

# Start bot
application.run_polling()
```

**Key Points**:
- Always `await query.answer()` to remove spinner
- Use `query.edit_message_text()` for inline keyboards (no new message)
- Store state in `context.user_data` for multi-step flows
- Keep callback_data short (max 64 chars)

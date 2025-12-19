# Telegram Keyboard Builders

```python
# keyboards.py
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Main menus
def main_menu():
    """Main navigation keyboard"""
    keyboard = [
        [KeyboardButton("🛍️ Buscar"), KeyboardButton("💰 Cupons")],
        [KeyboardButton("❤️ Salvos"), KeyboardButton("💬 Suporte")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def admin_menu():
    """Admin keyboard"""
    keyboard = [
        [KeyboardButton("📊 Estatísticas"), KeyboardButton("👥 Usuários")],
        [KeyboardButton("📝 Posts"), KeyboardButton("🔧 Configurações")],
        [KeyboardButton("🔙 Voltar")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Inline keyboards
def confirm_keyboard(action_id: str):
    """Confirmation dialog"""
    keyboard = [
        [
            InlineKeyboardButton("✅ Sim", callback_data=f"confirm_{action_id}"),
            InlineKeyboardButton("❌ Não", callback_data="cancel")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def pagination_keyboard(page: int, total_pages: int, prefix: str = "page"):
    """Pagination buttons"""
    buttons = []
    
    if page > 1:
        buttons.append(InlineKeyboardButton("⬅️", callback_data=f"{prefix}_{page-1}"))
    
    buttons.append(InlineKeyboardButton(f"{page}/{total_pages}", callback_data="noop"))
    
    if page < total_pages:
        buttons.append(InlineKeyboardButton("➡️", callback_data=f"{prefix}_{page+1}"))
    
    return InlineKeyboardMarkup([buttons])

def product_actions(product_id: int):
    """Product detail buttons"""
    keyboard = [
        [
            InlineKeyboardButton("📄 Detalhes", callback_data=f"product_{product_id}"),
            InlineKeyboardButton("🔗 Link", url="https://example.com")
        ],
        [
            InlineKeyboardButton("❤️ Salvar", callback_data=f"save_{product_id}"),
            InlineKeyboardButton("📤 Compartilhar", callback_data=f"share_{product_id}")
        ],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def category_keyboard():
    """Category selection"""
    keyboard = [
        [InlineKeyboardButton("🖥️ Tech", callback_data="cat_tech")],
        [InlineKeyboardButton("👗 Moda", callback_data="cat_fashion")],
        [InlineKeyboardButton("🏠 Casa", callback_data="cat_home")],
        [InlineKeyboardButton("🎮 Games", callback_data="cat_games")],
    ]
    return InlineKeyboardMarkup(keyboard)
```

## Usage

```python
# In message handler
await update.message.reply_text(
    "Bem-vindo! O que deseja fazer?",
    reply_markup=main_menu()
)

# In callback handler
await query.edit_message_text(
    text="Confirmar ação?",
    reply_markup=confirm_keyboard("delete_item_123")
)
```

**Tips**:
- Use emoji for visual clarity
- Max 2-3 buttons per row
- Always include "Back" button
- Use `callback_data` for actions (max 64 chars)
- Use `url` for external links

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "BOT_TOKEN"

MEMBERSHIP_LINK = "https://forms.gle/xob84oxbT3ntwgcm8"
SUPPORT_LINK = "https://revolut.me/alijvkg1"
FEEDBACK_LINK = "https://forms.gle/ToGunsuPmco9NyjZ9"


def menu():
    keyboard = [
        [InlineKeyboardButton("🤝 عضویت در انجمن", callback_data="membership")],
        [InlineKeyboardButton("💰 حمایت مالی", callback_data="support")],
        [InlineKeyboardButton("💡 انتقادات و پیشنهادات", callback_data="feedback")]
    ]
    return InlineKeyboardMarkup(keyboard)


def back_menu():
    keyboard = [
        [InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇮🇷 به ربات انجمن شیر و خورشید ایرانیان در مجارستان خوش آمدید\n\nلطفاً انتخاب کنید:",
        reply_markup=menu()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "membership":
        await query.edit_message_text(
            f"🤝 لینک عضویت:\n{MEMBERSHIP_LINK}",
            reply_markup=back_menu()
        )

    elif query.data == "support":
        await query.edit_message_text(
            f"💰 حمایت مالی:\n{SUPPORT_LINK}",
            reply_markup=back_menu()
        )

    elif query.data == "feedback":
        await query.edit_message_text(
            f"💡 انتقادات و پیشنهادات:\n{FEEDBACK_LINK}",
            reply_markup=back_menu()
        )

    elif query.data == "back":
        await query.edit_message_text(
            "🇮🇷 منوی اصلی",
            reply_markup=menu()
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot Started...")
app.run_polling()
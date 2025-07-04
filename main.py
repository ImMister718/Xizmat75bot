from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "ВСТАВЬ_ТУТ_СВОЙ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Такси", "Доставка", "Грузоперевозка"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет 👋\n\nЯ — бот-агрегатор. Мы связываем вас с водителями 🚗📦\n\nВыберите услугу:",
        reply_markup=reply_markup,
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

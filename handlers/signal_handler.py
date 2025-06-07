from telegram import Update
from telegram.ext import ContextTypes

async def signal_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📉 سیگنال خرید/فروش:\n(در این بخش به‌زودی سیگنال‌های خرید و فروش نمایش داده خواهد شد.)")

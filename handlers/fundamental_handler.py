from telegram import Update
from telegram.ext import ContextTypes

async def fundamental_analysis_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 تحلیل فاندامنتال:\n(در این بخش به‌زودی اطلاعات فاندامنتال نمایش داده خواهد شد.)")

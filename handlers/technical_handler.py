# handlers/technical_handler.py

from telegram import Update
from telegram.ext import ContextTypes
from utils.vip_manager import is_vip_user

async def technical_analysis_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if is_vip_user(user_id):
        # تحلیل تکنیکال حرفه‌ای ترکیب شده با فاندامنتال و اخبار
        await update.message.reply_text(
            "📈 تحلیل تکنیکال حرفه‌ای و فاندامنتال VIP:\n(اینجا تحلیل پیشرفته نمایش داده می‌شود)"
        )
    else:
        # تحلیل تکنیکال ساده برای کاربران عادی
        await update.message.reply_text(
            "📈 تحلیل تکنیکال ساده:\n(اینجا تحلیل تکنیکال ساده نمایش داده می‌شود)"
        )

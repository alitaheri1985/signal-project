from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main_keyboard import get_main_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به ربات تحلیل ارز دیجیتال خوش آمدید!", reply_markup=get_main_keyboard())

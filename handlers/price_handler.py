from telegram import Update
from telegram.ext import ContextTypes
from services.price_fetcher import get_bitcoin_price

async def bitcoin_price_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_bitcoin_price()
    await update.message.reply_text(f"💰 قیمت لحظه‌ای بیت‌کوین: {price}")

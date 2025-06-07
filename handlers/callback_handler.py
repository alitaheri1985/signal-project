from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, CallbackQueryHandler, filters

from handlers.price_handler import bitcoin_price_handler
from handlers.fundamental_handler import fundamental_analysis_handler
from handlers.technical_handler import technical_analysis_handler
from handlers.signal_handler import signal_handler
from handlers.vip_handler import (
    vip_payment_start,
    ask_for_receipt,
    receive_receipt,
    vip_verify_callback,
    ASK_FOR_RECEIPT
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(f"Received message: '{text}'")  # لاگ برای تست

    if text == "💰 قیمت بیت‌کوین":
        await bitcoin_price_handler(update, context)
    elif text == "📊 تحلیل فاندامنتال":
        await fundamental_analysis_handler(update, context)
    elif text == "📈 تحلیل تکنیکال":
        await technical_analysis_handler(update, context)
    elif text == "📉 سیگنال خرید/فروش":
        await signal_handler(update, context)
    elif text == "⭐ خرید اشتراک VIP":
        await vip_payment_start(update, context)
    else:
        await update.message.reply_text("دستور نامعتبر است.")

vip_conv_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex("^⭐ خرید اشتراک VIP$"), vip_payment_start)],
    states={
        ASK_FOR_RECEIPT: [
            MessageHandler(filters.Regex("^📤 پرداخت کردم$"), ask_for_receipt),
            MessageHandler(filters.PHOTO, receive_receipt),
        ]
    },
    fallbacks=[]
)

def register_vip_callback_handlers(application):
    application.add_handler(vip_conv_handler)
    application.add_handler(CallbackQueryHandler(vip_verify_callback, pattern=r"^vip_verify_"))

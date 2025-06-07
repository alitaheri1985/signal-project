import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters
)

from handlers.start_handler import start
from handlers.callback_handler import handle_message, vip_conv_handler
from handlers.vip_handler import vip_verify_callback
from utils.config import config

# راه‌اندازی لاگ
logging.basicConfig(level=logging.INFO)

def main():
    # ساختن اپلیکیشن ربات
    application = Application.builder().token(config["TELEGRAM_TOKEN"]).build()

    # افزودن هندلر پرداخت VIP و بررسی رسید (ابتدا)
    application.add_handler(vip_conv_handler)

    # افزودن هندلرهای اصلی (بعد از ConversationHandler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # هندلر CallbackQuery برای تایید/رد پرداخت
    application.add_handler(CallbackQueryHandler(vip_verify_callback, pattern="^vip_verify_"))

    print("🤖 ربات آماده است...")
    application.run_polling()

if __name__ == "__main__":
    main()

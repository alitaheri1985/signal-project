# keyboards/main_keyboard.py

from telegram import ReplyKeyboardMarkup

def get_main_keyboard():
    keyboard = [
        ["💰 قیمت بیت‌کوین", "📊 تحلیل فاندامنتال"],
        ["📈 تحلیل تکنیکال", "📉 سیگنال خرید/فروش"],
        ["⭐ خرید اشتراک VIP"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

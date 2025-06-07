from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from utils.config import config
from utils.vip_manager import add_vip_user
from keyboards.main_keyboard import get_main_keyboard

ASK_FOR_RECEIPT = 1

async def vip_payment_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "💎 برای فعال‌سازی اشتراک VIP:\n\n"
        "1️⃣ مبلغ مورد نظر را به آدرس تتر زیر واریز کنید:\n\n"
        f"`{config['TETHER_WALLET_ADDRESS']}`\n\n"
        "2️⃣ پس از واریز، روی دکمه زیر کلیک کنید و تصویر رسید را ارسال نمایید."
    )
    keyboard = [["📤 پرداخت کردم"]]
    await update.message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
        parse_mode="Markdown"
    )
    return ASK_FOR_RECEIPT

async def ask_for_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ لطفاً تصویر رسید پرداخت خود را ارسال کنید.")
    return ASK_FOR_RECEIPT

async def receive_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        user = update.effective_user
        caption = f"🧾 رسید پرداخت جدید از کاربر:\n@{user.username or 'بدون نام کاربری'}\nUserID: {user.id}"

        admin_id = config["ADMIN_ID"]
        photo_file = update.message.photo[-1].file_id
        await context.bot.send_photo(chat_id=admin_id, photo=photo_file, caption=caption)

        await update.message.reply_text(
            "✅ رسید شما دریافت شد و در حال بررسی است. نتیجه به زودی اطلاع داده خواهد شد.",
            reply_markup=ReplyKeyboardRemove()
        )

        await ask_admin_to_verify(update, context, user.id)

        return ConversationHandler.END

    else:
        await update.message.reply_text("❗️لطفاً فقط تصویر رسید را ارسال کنید.")
        return ASK_FOR_RECEIPT

async def ask_admin_to_verify(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id: int):
    keyboard = [
        [
            InlineKeyboardButton("✅ تایید", callback_data=f"vip_verify_yes_{user_id}"),
            InlineKeyboardButton("❌ رد", callback_data=f"vip_verify_no_{user_id}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    admin_id = config["ADMIN_ID"]
    await context.bot.send_message(
        chat_id=admin_id,
        text=f"رسید پرداخت جدید از کاربر {user_id} دریافت شد. لطفاً تایید یا رد کنید.",
        reply_markup=reply_markup
    )

async def vip_verify_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    parts = data.split("_")
    if len(parts) != 4:
        await query.edit_message_text("⚠️ داده نامعتبر است.")
        return

    action = parts[2]
    user_id = parts[3]

    if action == "yes":
        add_vip_user(user_id)
        await query.edit_message_text(f"✅ کاربر {user_id} به لیست VIP اضافه شد.")
        try:
            await context.bot.send_message(
                chat_id=int(user_id),
                text="🎉 اشتراک VIP شما تایید و فعال شد. از امکانات ویژه لذت ببرید!",
                reply_markup=get_main_keyboard()
            )
        except Exception as e:
            print(f"❗️ خطا در ارسال پیام به کاربر VIP {user_id}: {e}")
    else:
        await query.edit_message_text(f"❌ پرداخت کاربر {user_id} رد شد.")
        try:
            await context.bot.send_message(
                chat_id=int(user_id),
                text="❌ پرداخت شما تایید نشد. لطفاً با مدیر تماس بگیرید."
            )
        except Exception as e:
            print(f"❗️ خطا در ارسال پیام رد به کاربر {user_id}: {e}")

    return ConversationHandler.END

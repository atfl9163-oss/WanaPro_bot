import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# إعداد السجل (Logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# أمر البداية /start
async def start(command_update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = command_update.effective_user.first_name
    welcome_message = (
        f"أهلاً بك يا أسطورة {user_name} في بوت 'تغلي' الذكي! 🤖🔥\n"
        "أنا جاهز لتنفيذ مهامك التقنية، إدارة المحتوى، وتوليد السكربتات والأفكار.\n"
        "استخدم الأوامر المتاحة أو أرسل لي طلبك مباشرة!"
    )
    await command_update.message.reply_text(welcome_message)

# معالجة الرسائل والنصوص الواردة
async def handle_message(message_update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = message_update.message.text
    response_text = f"تم استلام طلبك يا أسطورة وجاري معالجته بنجاح: {user_text} ⚡"
    await message_update.message.reply_text(response_text)

def main():
    # تم دمج توكن البوت الخاص بك هنا مباشرة
    token = "8694566651:AAHmdGByWfuG3a-hNiGgZuNUA0g6pEAHx40"
    
    application = ApplicationBuilder().token(token).build()

    # تسجيل الأوامر والهاندلرز
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("🤖 بوت 'تغلي' يعمل الآن بكامل طاقته...")
    application.run_polling()

if __name__ == '__main__':
    main()
    

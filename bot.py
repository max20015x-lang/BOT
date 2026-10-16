import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد السجلات (Logs) للمساعدة في تصحيح الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دالة التعامل مع أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"أهلاً بك {user.mention_html()}! أنا بوت بسيط، يمكنك كتابة /help لمعرفة المزيد."
    )

# دالة التعامل مع أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("الأوامر المتاحة:\n/start - بدء البوت\n/help - قائمة المساعده")

def main():
    # جلب التوكين من متغير البيئة "BOT_TOKEN" بأمان
    # هذا هو الإعداد الذي ستقوم بضبطه على Render لاحقاً
    bot_token = os.environ.get("BOT_TOKEN")

    if not bot_token:
        logging.error("خطأ: لم يتم العثور على BOT_TOKEN في متغيرات البيئة.")
        return

    # إنشاء التطبيق (Application)
    application = Application.builder().token(bot_token).build()

    # إضافة معالجات الأوامر (Handlers)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # بدء البوت (Run Polling)
    # ملاحظة: للحفاظ على ساعات Render المجانية، يجب استخدام Webhooks لاحقاً،
    # لكن للبدء السريع والتجربة، سنستخدم run_polling().
    print("البوت يعمل الآن...")
    application.run_polling()

if __name__ == '__main__':
    main()

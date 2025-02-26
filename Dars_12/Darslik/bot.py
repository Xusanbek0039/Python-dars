from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Telegram bot tokenini shu yerga kiriting
TOKEN = "6849473588:AAEEt5wy0Mq3Dja3yJ--GXzRcavWqoev7_A"

# /start buyrug‘iga javob beruvchi funksiya
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Salom!")

# "qalesan" so‘ziga javob beruvchi funksiya
async def reply_qalesan(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    if "qalesan" in text:
        await update.message.reply_text("Yaxshi, o'zingiz yaxshimisiz?")
    elif "salom" in text:
        await update.message.reply_text("Yaxshi, o'zingiz yaxshimisiz?")



# Asosiy funksiya
def main():
    app = Application.builder().token(TOKEN).build()
    
    # /start buyrug‘ini qo‘shish
    app.add_handler(CommandHandler("start", start))
    
    # "qalesan" so‘zini ushlash uchun handler qo‘shish
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r"(?i)\bqalesan\b"), reply_qalesan))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r"(?i)\bsalom\b"), reply_qalesan))

    
    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()

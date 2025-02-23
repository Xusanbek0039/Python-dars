import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Bot tokeni
TOKEN = "6849473588:AAEEt5wy0Mq3Dja3yJ--GXzRcavWqoev7_A"

# Kanal usernamesi (ID o'rniga)
CHANNEL_USERNAME = "@IT_Creative_News"  # Kanal username'ini shu yerga yozing

# Raqamlar va ularga mos post ID'lar
VIDEOS = {
    "120": 337,  # 120 soni yozilsa, kanaldagi 337-postni yuborish
    "121": 338,  # 121 soni yozilsa, 338-post yuboriladi
    # Qo'shimcha raqamlar va post ID'larni qo'shing...
}

# Bot va dispatcher yaratish
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# /start komandasi
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("👋 Salom! Botga xush kelibsiz.\n\n📌 Istalgan raqam yuboring (masalan: 120, 121).")

# Kanal postlarini usernames orqali olib berish
@dp.message()
async def handle_message(message: Message):
    user_message = message.text

    if user_message in VIDEOS:
        post_id = VIDEOS[user_message]

        try:
            # Kanaldagi postni usernames orqali olish
            await bot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_USERNAME, message_id=post_id)
            await message.answer(f"✅ {user_message}-raqamga mos post yuborildi!")
        except Exception as e:
            await message.answer(f"⚠️ Xatolik yuz berdi: {e}")
    else:
        await message.answer("⚠️ Noto'g'ri raqam!\n\n📌 Iltimos, quyidagi raqamlardan birini yuboring:\n" + ", ".join(VIDEOS.keys()))

# Botni ishga tushirish
async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

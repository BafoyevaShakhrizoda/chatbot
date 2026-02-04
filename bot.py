import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


BOT_TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Salom 👋\nBu bot orqali menga anonim xabar yuborishingiz mumkin.\n"
        "Shunchaki xabaringizni yozing ✍️"               
                         )
    
@dp.message(lambda message: message.from_user.id == ADMIN_ID)
async def admin_reply(message: Message):
    replied_text = message.reply_to_message.text
    try:
        user_id = int(replied_text.split("🆔 ID: ")[1].split("\n")[0] 
        ) 
        await bot.send_message(
            user_id,
            f"📬 Admin javobi:\n\n{message.text}"
        )
        await message.answer("Javob yuborildi!")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")    
         
    
@dp.message()
async def forward_to_admin(message: types.Message):
    text = (
        "📩 Yangi xabar:\n\n"
        f"👤 From: @{message.from_user.username or 'Username yoq'}\n"
        f"🆔 ID: {message.from_user.id}\n\n"
        f"{message.text}"
    )
    await bot.forward(ADMIN_ID)
    await message.answer("Xabaringiz yuborildi! Rahmat 😊")
    
async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
    
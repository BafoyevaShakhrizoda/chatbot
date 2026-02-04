import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message


BOT_TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Salom 👋\nBu bot orqali menga anonim xabar yuborishingiz mumkin.\n"
        "Shunchaki xabaringizni yozing ✍️"               
                         )
@dp.message()
async def forward_to_admin(message: Message):
    text = (
        "📩 Yangi xabar:\n\n"
        f"👤 From: @{message.from_user.username}\n"
        f"🆔 ID: {message.from_user.id}\n\n"
        f"{message.text}"
    )
    await bot.send_message(ADMIN_ID, text)
    await message.answer("Xabaringiz yuborildi! Rahmat 😊")
    
async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
    
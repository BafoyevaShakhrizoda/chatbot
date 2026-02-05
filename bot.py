import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ContentType


BOT_TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu Alaykum, salomatmisiz?"              
                         )
    
@dp.message(lambda message: message.from_user.id == ADMIN_ID)
async def admin_reply(message: Message):
    replied_text = message.reply_to_message.text  or message.reply_to_message.caption or ""
    try:
        user_id = int(replied_text.split("🆔 ID: ")[1].split("\n")[0] ) 
        
        if message.text:
            await bot.send_message(user_id, f"📬 Admindan javob:\n\n{message.text}")
        elif message.photo:
            await bot.send_photo(user_id, message.photo[-1].file_id, 
                                   caption=f"📬 Admindan javob:\n\n{message.caption or ''}")
        elif message.video:
            await bot.send_video(user_id, message.video.file_id, 
                                   caption=f"📬 Admindan javob:\n\n{message.caption or ''}")
        elif message.document:
            await bot.send_document(user_id, message.document.file_id, 
                                   caption=f"📬 Admindan javob:\n\n{message.caption or ''}")
        
        await message.answer("Javob yuborildi!")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")    
         
    
@dp.message()
async def forward_to_admin(message: Message):
    text = (
        "📩 Yangi xabar:\n\n"
        f"👤 From: @{message.from_user.username or 'Username yoq'}\n"
        f"🆔 ID: {message.from_user.id}\n\n"
    )
    
    if message.text:
        text = f"📩 Yangi xabar:\n\n{user_info}{message.text}"
        await bot.send_message(ADMIN_ID, text)
        
    elif message.photo:
        caption = f"📩 Yangi xabar:\n\n{user_info}{message.caption or ''}"
        await bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption)
    
    elif message.video:
        caption = f"📩 Yangi xabar:\n\n{user_info}{message.caption or ''}"
        await bot.send_video(ADMIN_ID, message.video.file_id, caption=caption)
    
    elif message.document:
        caption = f"📩 Yangi xabar:\n\n{user_info}{message.caption or ''}"
        await bot.send_document(ADMIN_ID, message.document.file_id, caption=caption)
    
    
    
    await message.answer("Xabaringiz yuborildi! Rahmat 😊")


    
async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
    
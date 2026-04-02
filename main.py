import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, and_f
from aiogram.types import Message, ChatPermissions
from config import bot_token
import time


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(F.chat.type == "supergroup", and_f(F.text == "ban", F.reply_to_message))
async def get_bann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.ban_sender_chat(user_id)
   await message.answer(f"Siz guruhdan haydaldingiz\n ❌ {message.reply_to_message.from_user.full_name}")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.first_name}")

# @dp.message(F.text, F.chat.type == "supergroup")
# async def Guruhbot(message: Message):
#     chat_id = message.chat.id
#     turi = message.chat.type
#     await message.answer(f"Guruhlarimiz haqida\n{chat_id}\n{turi}")

# @dp.message(F.chat.type == "supergroup", F.new_chat_members)
# async def NewUserBot(message: Message):
#     for new in message.new_chat_members:
#         await message.answer(f"Assalomu alaykum {message.chat.title} ga xush kelibsiz\nBro {new.first_name}")

# @dp.message(F.chat.type == 'supergroup', F.left_chat_member )
# async def get_left_chat(message: Message):
#     await message.answer(f"Xayr bro {message.left_chat_member.full_name}")






@dp.message(F.chat.type == 'supergroup', and_f(F.text == "unban", F.reply_to_message))
async def get_unbann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.unban_sender_chat(user_id)
   await message.answer(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")




@dp.message(F.chat.type == 'supergroup', F.sticker)
async def BanUser(message: Message):
    user_id = message.from_user.id
    permsions = ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id, permsions)
    await message.answer("sticker yubormang odam qo'shsangiz ishlaydi")
    time.sleep(8)
    permsions = ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id, permsions)


@dp.message(F.chat.type == 'supergroup', and_f(F.text == "yozma", F.reply_to_message))
async def get_banned_chat(message: Message): 
    user_id = message.reply_to_message.from_user.id
    permsions = ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id, permsions)
    await message.answer(f"Siz notog'ri so'zdan foydlaandizngiz\n🚫 {message.reply_to_message.from_user.full_name}")



@dp.message(F.chat.type == 'supergroup',and_f(F.text == "yoz", F.reply_to_message))
async def get_not_ban_chat(message: Message):
    user_id = message.reply_to_message.from_user.id
    permsions = ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id, permsions)
    await message.answer(f"Siz endi yoza olasiz\n🆗 {message.reply_to_message.from_user.full_name}")




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("bilmayman")
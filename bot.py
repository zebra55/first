import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token='1011989128:AAH1lakCGEn-yRXj1e6S9emFDe-HcJy2jIc')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)



if __name__ == '__main__':
    executor.start_polling(dp)
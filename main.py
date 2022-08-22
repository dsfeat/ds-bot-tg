from aiogram import Bot, Dispatcher, executor, types
import python_weather

# сам бот
bot = Bot(token='5712683923:AAF7hA_vCqFkxREb62lPO-A9f4-NbB6M_kY')
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

# эхо
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + '\n'
    resp_msg += f'Температура на данный момент: {celsius}° C\n'
    resp_msg += f'Состояние погоды: {weather.current.sky_text}'

    await message.answer(resp_msg)

    

# рон-поллинг
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
from aiogram import Router, types
from aiogram.filters import Command
from config import bot, ADMINS, ARIES
from keyboard import what_is_your_horoscope_symbol
from parser import get_pred

router = Router()


@router.message(Command('start'))
async def who_are_you(message: types.Message | types.CallbackQuery):
    if message.from_user.id in ARIES:
        await message.answer('Куда скидывать овну (денег)?, Пиши сюда.')
    else:
        if isinstance(message, types.Message):
            await message.answer(text='Для какого знака Вам нужно предсказание?',
                                 reply_markup=what_is_your_horoscope_symbol(),
                                 disable_notification=True)
        else:
            await message.message.answer(text='Для какого знака Вам нужно предсказание?',
                                         reply_markup=what_is_your_horoscope_symbol(),
                                         disable_notification=True)


@router.callback_query()
async def really_prediction(callback: types.CallbackQuery):
    if get_pred(callback.data)[-1] == '.':

        await callback.message.edit_text(f"{get_pred(callback.data)[:-1]}, а также, {'вам предначертано перевести денег овну' if callback.data != 'aries' else 'судьба велит вам получить много денег'}")
    else:
        await callback.message.edit_text(f"{'Вам предначертано перевести денег овну' if callback.data != 'aries' else 'Получите много денег'}. {get_pred(callback.data)}")
    await who_are_you(callback)
    await callback.answer()


@router.message()
async def where_send_money(message: types.Message):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=message.text)
    await message.answer('Спасибо! Скоро это появится в этом боте (если он включен).')
    if isinstance(message, types.Message):
        await message.answer(text='Для какого знака Вам нужно предсказание?',
                             reply_markup=what_is_your_horoscope_symbol(),
                             disable_notification=True)
    else:
        await message.message.answer(text='Для какого знака Вам нужно предсказание?',
                                     reply_markup=what_is_your_horoscope_symbol(),
                                     disable_notification=True)
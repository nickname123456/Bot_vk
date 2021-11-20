from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Blueprint
from sqlighter import SQLighter
from settings import smiles, greetings
import random


db = SQLighter('bot_vk.db')
bp = Blueprint('menu')
bp.on.vbml_ignore_case = True




#Если написали "Меню" или нажали на соответствующую кнопку
@bp.on.message(text=["Меню", 'Главное меню', 'гм', 'gm'])
@bp.on.message(payload={'cmd': 'menu'})
async def menu(message: Message):
    userInfo = await bp.api.users.get(message.from_id)
    userInfo = userInfo[0]

    keyboard = (
        Keyboard()
        .add(Text('Магазин', {'cmd': 'shop'}), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Рабочее место', {'cmd': 'workplace'}), color=KeyboardButtonColor.SECONDARY)
        .add(Text('Дубль карты', {'cmd': 'two_maps'}), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text('Профиль', {'cmd': 'profile'}), color=KeyboardButtonColor.PRIMARY)
        .add(Text('⚙', {'cmd': 'settings'}), color=KeyboardButtonColor.PRIMARY)
    )

    if db.get_city(userInfo.id) == 'родная деревня':
        await message.answer(f'{random.choice(smiles)}{random.choice(greetings)} {db.get_nickname(userInfo.id)}, ты сейчас в  поселении {db.get_city(userInfo.id)}! \n💰Баланс:{db.get_balance(userInfo.id)}', keyboard=keyboard)
    
    else:
        await message.answer(f'{db.get_nickname(userInfo.id)}, ты сейчас в  городе {db.get_city(userInfo.id)}! \n💰Баланс:{db.get_balance(userInfo.id)}', keyboard=keyboard)
import asyncio
from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Blueprint
from vkbottle.tools.dev_tools.mini_types.bot import message
from sqlighter import SQLighter


db = SQLighter('bot_vk.db')
bp = Blueprint('menu')
bp.on.vbml_ignore_case = True



#Если написали "Меню" или нажали на соответствующую кнопку
@bp.on.message(text=["Начать"])
@bp.on.message(payload={'cmd': 'start'})
async def menu(message: Message):
    userInfo = await bp.api.users.get(message.from_id)
    userInfo = userInfo[0]
    
    if db.get_nickname(userInfo.id) is None:
        keyboard = (
            Keyboard()
            .add(Text('Выбрать название канала', {'cmd': 'nick'}), color=KeyboardButtonColor.SECONDARY)
        )

        db.add_user(userInfo.id, 'NoName', 0)
        db.commit()

        text = 'Одним обычным, скучным вечером, ты смотря своих любимых блогеров, думал о том, как много зарабатывать не угробя при этом пол жизни, обучаясь, как вдруг к тебе пришла идея: "а почему мне самому не стать ютубером?". С этого момента начался твой долгий, но интересный путь к славе...'
        await message.answer(text, keyboard=keyboard, attachment='photo-198179933_457239073')

        await asyncio.sleep(1)

        text = '🤔Итак... Тебе нужно придумать название своего канала (ник). Выберай хорошо, так как чем оригинальней будет название - тем ты будешь популярней! \n⚙В любой момент ты можешь поменять его в настройках.'
        await message.answer(text, keyboard=keyboard)
    
    else:
        keyboard = (
        Keyboard()
        .add(Text('Главное меню', {'cmd': 'menu'}), color=KeyboardButtonColor.SECONDARY)
        )

        await message.answer('Ты уже начал свой путь.', keyboard=keyboard)
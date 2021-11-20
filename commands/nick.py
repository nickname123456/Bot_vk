from vkbottle.bot import Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Blueprint
from vkbottle.tools.dev_tools import keyboard
from sqlighter import SQLighter
from vkbottle import CtxStorage
from vkbottle_types import BaseStateGroup


bp = Blueprint('schedule_download')
bp.on.vbml_ignore_case = True

db = SQLighter('bot_vk.db')

ctx = CtxStorage()

class ChangeNick(BaseStateGroup):
    nick = 0



@bp.on.message(lev=['ник', 'Выбрать название канала', 'сменить ник', 'nick'])
async def nick(message: Message):
    await bp.state_dispenser.set(message.peer_id, ChangeNick.nick)
    return "Напиши свой никнейм"

@bp.on.message(state=ChangeNick.nick)
async def nick_handler(message: Message):
    await bp.state_dispenser.delete(message.peer_id)

    userInfo = await bp.api.users.get(message.from_id)
    userInfo = userInfo[0]

    nick = message.text

    db.edit_nickname(userInfo.id, nick)
    db.commit()

    keyboard = (
        Keyboard()
        .add(Text('Главное меню', {'cmd': 'menu'}), color=KeyboardButtonColor.SECONDARY)
        )

    await message.answer(f'Ты успешно сменил свой никнейм на: {nick}', keyboard=keyboard)

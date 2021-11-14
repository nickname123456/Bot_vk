from vkbottle import Bot
from commands import bps
from settings import token

bot = Bot(token=token)

#Список дневников учеников
#diarys = {}

print('')
print('-------------------------------')
print('  Скрипт Бот Ютубер запущен.')
print('  Разработчик: Кирилл Арзамасцев ')
print('  https://vk.com/kirillarz')
print('-------------------------------')
print('')

for bp in bps:
    bp.load(bot)

bot.run_forever()

# -- coding: utf-8 --

import asyncio
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import json
import time
import sqlite3




print('')
print('-------------------------------')
print('  Скрипт Бот Ютубер запущен.')
print('  Разработчик: Кирилл Арзамасцев ')
print('  https://vk.com/kirillarz')

print('-------------------------------')
print('')



# вписываем свой токен
token = "1b464e0c8f92ffaef1fa2b921bdd396d2062014bef32657eb1e7b62aa0d4fb36a2555fb5e6383cbadcfc4"
vk_session = vk_api.VkApi(token=token)

# тип авторизация
session_api = vk_session.get_api()
longpoll    = VkLongPoll(vk_session)


###################################################################################################
#vk.method('wall.post', {                                                                         ##
#           'owner_id': OWNER_ID,                                                                ##
#          'message': 'Хей!',                                                                   ##
#            'attachments': href,                                                                 ##
#        })                                                                                       ##
###################################################################################################



# ```````````````````````````````````````СОЗДАЕМ ВСЕ ПЕРЕМЕННЫЕ`````````````````````````````````````````````````````
users_id    = []
inventory   = {}
balance     = {}
nicks       = {}
admins      = {}
cities      = {}
inventory   = {}
check_start = {} # Проверка на нажатие кнопки старт в начале
id_admin    = 457641188
photo       = None
# приветствия
greetings = ['привет', 'здарова', 'ку', 'салам', 'hi', 'хай', 'бонжур', 'здравствуй', 'здравствуйте','добрый день', 'добрый вечер','доброе утро', 'салют','приветик'] 
# смайлики
smiles = ['😀','😃','😄','😁','😆','😅','😂','🤣','☺','😊','😇','🙂','🙃','😉','😌','😜','😝','🤑','🤡','🥳','🤩''😎','🤓','🧐','🤨','🤠','😏','🥺','😑','😐','😯','😦','😧','😮','🥱','😵','😳','😱','😨','😰','😷','🤧','🤮','🥴','🤕','🤒','👿','😈','👻','💀','💩','👺','👽','👨‍💻']
rotateWord = {
    ' ': ' ',
    'q': 'q',
    'w': 'ʍ',
    'e': 'ǝ',
    'r': 'ɹ',
    't': 'ʇ',
    'y': 'ʎ',
    'u': 'u',
    'i': 'ᴉ',
    'o': 'o',
    'p': 'p',
    'a': 'ɐ',
    's': 's',
    'd': 'd',
    'f': 'ɟ',
    'g': 'ƃ',
    'h': 'ɥ',
    'j': 'ɾ',
    'k': 'ʞ',
    'l': 'l',
    'z': 'z',
    'x': 'x',
    'c': 'ɔ',
    'v': 'ʌ',
    'b': 'b',
    'n': 'n',
    'm': 'ɯ',

    'й': 'ņ',
    'ц': 'ǹ',
    'у': 'ʎ',
    'к': 'ʞ',
    'е': 'ǝ',
    'н': 'н',
    'г': 'ɹ',
    'ш': 'm',
    'щ': 'm',
    'з': 'ε',
    'х': 'х',
    'ъ': 'q',
    'ф': 'ф',
    'ы': 'ıq',
    'в': 'ʚ',
    'а': 'ɐ',
    'п': 'u',
    'р': 'd',
    'о': 'о',
    'л': 'v',
    'д': 'ɓ',
    'ж': 'ж',
    'э': 'є',
    'я': 'ʁ',
    'ч': 'һ',
    'с': 'ɔ',
    'м': 'w',
    'и': 'и',
    'т': 'ɯ',
    'ь': 'q',
    'б': 'ƍ',
    'ю': 'oı'
}

translateWord = { 
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    '[': 'х',
    ']': 'ъ',
    'a': 'ф',
    's': 'ы',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    ';': 'ж',
    "'": 'э',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    ',': 'б',
    '.': 'ю',
    '/': '.',
    ' ': ' ',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0',
    '-': '-',
    '=': '='
}



#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#```````````````````````````````````````````````ДЕРЕВНЯ```````````````````````````````````````````````````````````
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````
cameras_rodnayaDerevnya = {
    'NoName Webcam rev. 1.0': {'cost': 75, 'gain': 0.0001, 'photo': 'photo-198179933_457239079'},
    'NoName Webcam rev. 2.0': {'cost': 125, 'gain': 0.0005, 'photo': 'photo-198179933_457239080'},
    'NoName Webcam rev. 3.0': {'cost': 200, 'gain': 0.001, 'photo': 'photo-198179933_457239081'},
    'CBR CW-835M': {'cost': 300, 'gain': 0.005, 'photo': 'photo-198179933_457239082'},
    'NoName Webcam rev. 4.0': {'cost': 450, 'gain': 0.01, 'photo': 'photo-198179933_457239083'},
    'CBR CW 840M': {'cost': 650, 'gain': 0.05, 'photo': 'photo-198179933_457239084'},
    'Banggood CMOS 50M': {'cost': 850, 'gain': 0.1, 'photo': 'photo-198179933_457239085'},
    'Defender C-090': {'cost': 1100, 'gain': 0.4, 'photo': 'photo-198179933_457239086'},
    'GRES electroniks': {'cost': 1400, 'gain': 0.7, 'photo': 'photo-198179933_457239087'}
}


microphone_rodnayaDerevnya = {
    'CD-2000': {'cost': 75, 'gain': 0.0001, 'photo': 'photo-198179933_457239129'},
    'Sven MK-150': {'cost': 125, 'gain': 0.0005, 'photo': 'photo-198179933_457239130'},
    'MIC-109 Defender': {'cost': 200, 'gain': 0.001, 'photo': 'photo-198179933_457239131'},
    'MIC-117 Defender': {'cost': 300, 'gain': 0.005, 'photo': 'photo-198179933_457239132'},
    'Sven MK-205': {'cost': 450, 'gain': 0.01, 'photo': 'photo-198179933_457239133'},
    'Aceline AMIC-30': {'cost': 650, 'gain': 0.05, 'photo': 'photo-198179933_457239134'},
    'Ritmix RDM-125': {'cost': 850, 'gain': 0.1, 'photo': 'photo-198179933_457239135'},
    'BEHRINGER C-1U': {'cost': 1100, 'gain': 0.4, 'photo': 'photo-198179933_457239136'},
    'Trust GTX 232 Mantis': {'cost': 1400, 'gain': 0.7, 'photo': 'photo-198179933_457239137'}
    #'DM800': {'cost': 2000, 'gain': 1.0, 'photo': 'photo-198179933_457239138'}
}


keyboard_rodnayaDerevnya = {
    'NoName keyboard rev. 1.0': {'cost': 75, 'gain': 0.0001, 'photo': 'photo-198179933_457239088'},
    'NoName keyboard rev. 2.0': {'cost': 125, 'gain': 0.0005, 'photo': 'photo-198179933_457239089'},
    'Oklick 120M': {'cost': 200, 'gain': 0.001, 'photo': 'photo-198179933_457239090'},
    'ExeGate LY-403': {'cost': 300, 'gain': 0.005, 'photo': 'photo-198179933_457239091'},
    'Defender HB-420': {'cost': 450, 'gain': 0.01, 'photo': 'photo-198179933_457239092'},
    'Perfeo PF-8801': {'cost': 650, 'gain': 0.05, 'photo': 'photo-198179933_457239093'},
    'Гарнизон GK-100': {'cost': 850, 'gain': 0.1, 'photo': 'photo-198179933_457239094'},
    'Ritmix RKB-151': {'cost': 1100, 'gain': 0.4, 'photo': 'photo-198179933_457239095'},
    'Smartbuy SBK-221U-K': {'cost': 1400, 'gain': 0.7, 'photo': 'photo-198179933_457239096'}
}


mouse_rodnayaDerevnya = {
    'Partner Precise CM-010': {'cost': 75, 'gain': 0.0001, 'photo': 'photo-198179933_457239098'},
    'Limeide XF-240': {'cost': 125, 'gain': 0.0005, 'photo': 'photo-198179933_457239099'},
    'Patch MS-759': {'cost': 200, 'gain': 0.001, 'photo': 'photo-198179933_457239100'},
    'Ritmix ROM-111': {'cost': 300, 'gain': 0.005, 'photo': 'photo-198179933_457239101'},
    'Optimum MB-160': {'cost': 450, 'gain': 0.01, 'photo': 'photo-198179933_457239102'},
    'Oklick 115S': {'cost': 650, 'gain': 0.05, 'photo': 'photo-198179933_457239103'},
    'Oklick 225M': {'cost': 850, 'gain': 0.1, 'photo': 'photo-198179933_457239104'},
    'Defender Optimum MB-270': {'cost': 1100, 'gain': 0.4, 'photo': 'photo-198179933_457239105'},
    'Ritmix WM-984': {'cost': 1400, 'gain': 0.7, 'photo': 'photo-198179933_457239106'}
}


monitor_rodnayaDerevnya = {
    'LG Flatron 1400x': {'cost': 550, 'gain': 1, 'photo': 'photo-198179933_457239107'},
    'SAMSUNG SperMonitor 720x': {'cost': 900, 'gain': 4, 'photo': 'photo-198179933_457239108'},
    'LG flatron ez T710BH': {'cost': 1650, 'gain': 7, 'photo': 'photo-198179933_457239109'},
    'PHILIPS wb 107': {'cost': 2000, 'gain': 7.5, 'photo': 'photo-198179933_457239110'},
    'LG flatron F700P': {'cost': 3100, 'gain': 10, 'photo': 'photo-198179933_457239111'},
    'ViewSonic T927VI': {'cost': 3700, 'gain': 11.1, 'photo': 'photo-198179933_457239112'},
    'SAMSUNG SperMonitor x875': {'cost': 4500, 'gain': 18, 'photo': 'photo-198179933_457239113'},
    'LG flatron F967K': {'cost': 6000, 'gain': 23, 'photo': 'photo-198179933_457239115'},
    'Acer v173': {'cost': 8100, 'gain': 28.88888, 'photo': 'photo-198179933_457239116'}
}















#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#```````````````````````````````````````````````ЧЕЛЯБИНСК```````````````````````````````````````````````````````````
#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````



cameras_сhelyabinsk = {
    'ExeGate BlackView C310': {'cost': 2000, 'gain': 1, 'photo': 'photo-198179933_457239118'},
    'Logitech QuickCam Deluxe': {'cost': 2200, 'gain': 1.01, 'photo': 'photo-198179933_457239119'},
    'Trust Exis Webcam': {'cost': 2700, 'gain': 1.04, 'photo': 'photo-198179933_457239121'},
    'ExeGate BusinessPro C922 HD': {'cost': 3000, 'gain': 1.05, 'photo': 'photo-198179933_457239122'},
    'Canyon CNE-CWC1': {'cost': 4285, 'gain': 1.75, 'photo': 'photo-198179933_457239123'},
    'Genius FaceCam 1000X HD': {'cost': 4999, 'gain': 2, 'photo': 'photo-198179933_457239124'},
    'Trust SpotLight Webcam Pro': {'cost': 5439, 'gain': 2.3333, 'photo': 'photo-198179933_457239126'},
    'WZ1': {'cost': 6199, 'gain': 2.63, 'photo': 'photo-198179933_457239127'},
    'Logitech QuickCam Communicate Delux': {'cost': 6700, 'gain': 2.9991, 'photo': 'photo-198179933_457239125'}
}


microphone_сhelyabinsk = {
    'Ritmix RDM-130': {'cost': 2000, 'gain': 0.8, 'photo': 'photo-198179933_457239139'},
    'DM800': {'cost': 2200, 'gain': 1.0, 'photo': 'photo-198179933_457239138'},
    'BBK CM110': {'cost': 2700, 'gain': 1.01, 'photo': 'photo-198179933_457239140'},
    'Ritmix RDM-131': {'cost': 3000, 'gain': 1.04, 'photo': 'photo-198179933_457239141'},
    'BLAST BAM-101': {'cost': 4285, 'gain': 1.05, 'photo': 'photo-198179933_457239142'},
    'BBK CM215': {'cost': 4999, 'gain': 1.75, 'photo': 'photo-198179933_457239143'},
    'BBK CM132': {'cost': 5439, 'gain': 2, 'photo': 'photo-198179933_457239145'},
    'Trust GXT 239 Nepa': {'cost': 6199, 'gain': 2.3333, 'photo': 'photo-198179933_457239146'},
    'WSTER WS-858': {'cost': 6700, 'gain': 2.63, 'photo': 'photo-198179933_457239144'}
}


keyboard_сhelyabinsk = {
    'ExeGate LY-331L2': {'cost': 2000, 'gain': 0.8, 'photo': 'photo-198179933_457239147'},
    'Dialog KS-030P': {'cost': 2200, 'gain': 1, 'photo': 'photo-198179933_457239148'},
    'ExeGate LY-403': {'cost': 2700, 'gain': 1.01, 'photo': 'photo-198179933_457239149'},
    'Gembird KB-G530L': {'cost': 3000, 'gain': 1.04, 'photo': 'photo-198179933_457239150'},
    'Logitech Wireless Combo MK240': {'cost': 4285, 'gain': 1.05, 'photo': 'photo-198179933_457239151'},
    'A4 Tech KV-300H': {'cost': 4999, 'gain': 1.75, 'photo': 'photo-198179933_457239152'},
    'Logitech Keyboard K120': {'cost': 5439, 'gain': 2, 'photo': 'photo-198179933_457239153'},
    'Redragon Shiva': {'cost': 6199, 'gain': 2.33333, 'photo': 'photo-198179933_457239154'},
    'Red Square Tesla TKL RGB': {'cost': 6700, 'gain': 2.63, 'photo': 'photo-198179933_457239155'}
}


mouse_сhelyabinsk = {
    '': {'cost': 75, 'gain': 0.0001, 'photo': 'photo-198179933_457239098'},
    '': {'cost': 125, 'gain': 0.0005, 'photo': 'photo-198179933_457239099'},
    '': {'cost': 200, 'gain': 0.001, 'photo': 'photo-198179933_457239100'},
    '': {'cost': 300, 'gain': 0.005, 'photo': 'photo-198179933_457239101'},
    '': {'cost': 450, 'gain': 0.01, 'photo': 'photo-198179933_457239102'},
    '': {'cost': 650, 'gain': 0.05, 'photo': 'photo-198179933_457239103'},
    '': {'cost': 850, 'gain': 0.1, 'photo': 'photo-198179933_457239104'},
    '': {'cost': 1100, 'gain': 0.4, 'photo': 'photo-198179933_457239105'},
    '': {'cost': 1400, 'gain': 0.7, 'photo': 'photo-198179933_457239106'}
}


monitor_сhelyabinsk = {
    '': {'cost': 550, 'gain': 1, 'photo': 'photo-198179933_457239107'},
    '': {'cost': 900, 'gain': 4, 'photo': 'photo-198179933_457239108'},
    '': {'cost': 1650, 'gain': 7, 'photo': 'photo-198179933_457239109'},
    '': {'cost': 2000, 'gain': 7.5, 'photo': 'photo-198179933_457239110'},
    '': {'cost': 3100, 'gain': 10, 'photo': 'photo-198179933_457239111'},
    '': {'cost': 3700, 'gain': 11.1, 'photo': 'photo-198179933_457239112'},
    '': {'cost': 4500, 'gain': 18, 'photo': 'photo-198179933_457239113'},
    '': {'cost': 6000, 'gain': 23, 'photo': 'photo-198179933_457239115'},
    '': {'cost': 8100, 'gain': 28.88888, 'photo': 'photo-198179933_457239116'}
}


# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````














# создание кнопок
keyboard = {"buttons":[],"one_time":True}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))






# ````````````````````````````````````ВСЕ ФУНКЦИИ```````````````````````````````````:
# сохранения переменных
def save(name, what):
    file = open(str(name), "w", encoding='utf-8')
    what = str(what)
    file.write( what )
    file.close()




# Загрузка фото на сервер ВК, для дальнейшего использования
def upload_photo(x):
    global photo

    uploader = vk_api.upload.VkUpload(vk_session)
    img = uploader.photo_messages(x)
    media_id = str(img[0]['id'])
    owner_id = str(img[0]['owner_id'])
    photo = 'photo' + owner_id + '_' + media_id





# отправить сообщение
def send(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text , 'keyboard' : keyboard , 'attachment' : photo , 'random_id': 0})




# Отправка рассылки
async def mailing(msg):
    if admins[id] == 'yes':
        text = msg[9 : ]
        for i in users_id:
            send(i, text)
    else:
        send(id, 'Недостаточно прав!')




async def nick():
    global photo

    photo = None
    send(id, "🙃Какое название канала ты хочешь?")

    for event in longpoll.listen():

        await asyncio.sleep(0.5)

        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user and not event.from_me:
                msg = event.text
                if id == event.user_id:
                        send(id, 'Ты успешно сменил ник на "' + msg + '"!')
                        nicks[id] = msg

                        break




async def gm():
    global keyboard

    if cities[id] == 'родная деревня':

        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": "Магазин"
                        },
                        "color": "secondary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "Рабочее место"
                        },
                        "color": "secondary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "Дубль карты"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Профиль"
                        },
                        "color": "primary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "⚙"
                        },
                        "color": "primary"
                    }
                ]
            ]
        }

        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))

        photo = None


        await send(id, random.choice(smiles) + random.choice(greetings) + ' ' + str(nicks[id]) + ', ты сейчас в  поселении "' + cities[id] + '! \n💰Баланс: '+str(balance[id]))
    else:

        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": "Магазин"
                        },
                        "color": "secondary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "Рабочее место"
                        },
                        "color": "secondary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "Дубль карты"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Профиль"
                        },
                        "color": "primary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "⚙"
                        },
                        "color": "primary"
                    }
                ]
            ]
        }

        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))

        photo = None


        await send(id, random.choice(smiles) + random.choice(greetings) + ' ' + str(nicks[id]) + ', ты сейчас в  городе "' + cities[id] + '"! \n💰Баланс: '+str(balance[id]))











async def rotateText(x):
    x = x[10:]    # срезаем то, что нужно
    y = len(x)    # вычитаем длину текста, для того чтобы его перевернуть
    x = x[y: :-1] # переворачиваем текст по х
    text = ''     # обозачаем то, что текст-строка
    for i in x:
        if i in rotateWord:      # если буква есть в нашем словаре
            word = rotateWord[i] # переворачиваем букву по у
            text += word         # добавляем новую букву в перевернутый по х и у текст
        else:
            send(id, 'Хммммм! Символа "'+i+'" нет в моей библиотеке. Поэтому пропущу его!') # если символа нет в нашей библиотеки
    send(id, text) # отправляем текст игроку




async def translateText(x):
    x = x.lower()
    text = ''     # обозачаем то, что текст-строка
    for i in x:
        if i in translateWord:      # если буква есть в нашем словаре
            word = translateWord[i] # заменяем inglish букву на русскую
            text += word         # добавляем новую букву в перевернутый по х и у текст
        else:
            send(id, 'Хммммм! Символа "'+i+'" нет в моей библиотеке. Поэтому пропущу его!') # если символа нет в нашей библиотеки
            send(id_admin, 'Добавь символ "' + str(i) + '" в функцию translateText')
    send(id, text) # отправляем текст игроку







def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)


    return Seconds






async def starting():
    if id not in users_id:
        upload_photo('17-kak-stat-populyarnym-na-youtube.jpg')
        start_text = 'Одним обычным, скучным вечером, ты смотря своих любимых блогеров, думал о том, как много зарабатывать не угробя при этом пол жизни, обучаясь, как вдруг к тебе пришла идея: "а почему мне самому не стать ютубером?". С этого момента начался твой долгий, но интересный путь к славе...'
        send(id, start_text)
        await asyncio.sleep(7)

        upload_photo('thinking-face-facebook.png')
        send(id, '🤔Итак... Тебе нужно придумать название своего канала (ник). Выбирай хорошо, так как чем оригинальней будет название - тем ты будешь популярней! \n⚙В любой момент ты можешь поменять его в настройках.')
        await asyncio.sleep(6)
        nick()

        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": "Главное меню"
                        },
                        "color": "secondary"
                    }
                ]
            ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))

        upload_photo('загружено.jpg')
        
        send(id, 'Хорошо, теперь ты можешь ознакомиться с правилами (еще не готово, прости)')

        users_id += id
        balance[id] = 0
        admins = 'no'
        cities[id] = 'родная деревня'
        houses[id] = 'улица'







async def shop():

    start = time.time() # во сколько человек зашел в магазин



    if cities[id] == 'родная деревня':
        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": 'Электротовары'
                        },
                        "color": "secondary"
                    },
                    {
                        "action": {
                            "type": "text",
                            "label": "PCStore"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Главное меню"
                        },
                        "color": "primary"
                    }
                ]
            ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))

        photo = None

        send(id, 'В какой магазин пойдем?')

        msg = None

        for event2 in longpoll.listen():
            await asyncio.sleep(0.5)
            if time.time() - start >= 45:
                if event2.user_id != id:
                    send(event2.user_id, '😕 попробуй ещё раз')

                send(id, 'Прости, но ты слишком долго думал, и мне пришлось пренести тебя в гм((((((')
                gm()

                end = time.time()         
                print(end-start)

                break
            if event2.type == VkEventType.MESSAGE_NEW:
                if event2.from_user and not (event2.from_me): # если сообщение НЕ от бота
                    msg = event2.text
                    check = 1
                    if id == event2.user_id:

                        if msg == 'Электротовары':

                            photo = None
                            keyboard = {
                                "one_time": True,
                                "buttons": [
                                    [{
                                            "action": {
                                                "type": "text",
                                                "label": "Камеры"
                                            },
                                            "color": "secondary"
                                        },
                                        {
                                            "action": {
                                                "type": "text",
                                                "label": "Микрофоны"
                                            },
                                            "color": "secondary"
                                        },
                                        {
                                            "action": {
                                                "type": "text",
                                                "label": "Мышки"
                                            },
                                            "color": "secondary"
                                        }],
                                        [{
                                            "action": {
                                                "type": "text",
                                                "label": "Мониторы"
                                            },
                                            "color": "secondary"
                                        },
                                        {
                                            "action": {
                                                "type": "text",
                                                "label": "Клавиатуры"
                                            },
                                            "color": "secondary"
                                        }],
                                        [{
                                            "action": {
                                                "type": "text",
                                                "label": "Назад"
                                            },
                                            "color": "primary"

                                        }
                                    ]
                                ]
                            }

                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                            keyboard = str(keyboard.decode('utf-8'))
                            send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')

                            for event in longpoll.listen():
                                await asyncio.sleep(0.5)
                                if time.time()-start >= 45:
                                    if event.user_id != id:
                                        send(event.user_id, '😕 попробуй ещё раз')
                                        break
                                if event.type == VkEventType.MESSAGE_NEW:
                                    if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                        msg = event.text
                                        check = 1
                                        if id == event.user_id:

                                            if msg == 'Назад':
                                                keyboard = {
                                                    "one_time": True,
                                                    "buttons": [
                                                        [{
                                                                "action": {
                                                                    "type": "text",
                                                                    "label": 'Электротовары'
                                                                },
                                                                "color": "secondary"
                                                            },
                                                            {
                                                                "action": {
                                                                    "type": "text",
                                                                    "label": "PCStore"
                                                                },
                                                                "color": "secondary"
                                                            }],
                                                            [{
                                                                "action": {
                                                                    "type": "text",
                                                                    "label": "Главное меню"
                                                                },
                                                                "color": "primary"
                                                            }
                                                        ]
                                                    ]
                                                }
                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                photo = None

                                                send(id, 'В какой магазин пойдем?')
                                                break


                                            elif msg == 'Камеры':

                                                keyboard = {"one_time": True, "buttons": list(range(0, len(cameras_rodnayaDerevnya) + 1))}
                                                
                                                score = 0
                                                for item in cameras_rodnayaDerevnya:
                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                    score += 1

                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                send(id, 'Вот все доступные вэбки:')

                                                for event in longpoll.listen():
                                                    await asyncio.sleep(0.5)
                                                    if time.time()-start >= 45:
                                                        if event.user_id != id:
                                                            send(event.user_id, '😕 попробуй ещё раз')
                                                        break
                                                    if event.type == VkEventType.MESSAGE_NEW:
                                                        if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                            msg = event.text
                                                            if id == event.user_id:
                                                                if msg in cameras_rodnayaDerevnya:
                                                                    item = msg
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Купить"
                                                                                    },
                                                                                    "color": "positive"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"
                                                                                }
                                                                            ]
                                                                                
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))

                                                                    send(id, 'Название: ' + msg + '\n Цена: ' + str(cameras_rodnayaDerevnya[msg]['cost']) + '\n усиление: ' + str(cameras_rodnayaDerevnya[msg]['gain']))
                                                                    
                                                                    for event in longpoll.listen():
                                                                        await asyncio.sleep(0.5)
                                                                        if time.time()-start >= 45:
                                                                            if event.user_id != id:
                                                                                send(event.user_id, '😕 попробуй ещё раз')
                                                                            break
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                                                msg = event.text
                                                                                if id == event.user_id:
                                                                                    if msg == 'Купить':
                                                                                        if balance[id] >= cameras_rodnayaDerevnya[item]['cost']:
                                                                                            inventory[id]['camera']['name'] = item
                                                                                            inventory[id]['camera']['cost'] = cameras_rodnayaDerevnya[item]['cost'] / 2
                                                                                            inventory[id]['camera']['gain'] = cameras_rodnayaDerevnya[item]['gain']
                                                                                            inventory[id]['camera']['photo'] = cameras_rodnayaDerevnya[item]['photo']
                                                                                            balance[id] -= cameras_rodnayaDerevnya[item]['cost']
                                                                                            
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239072%2Falbum-198179933_277009630'

                                                                                            send(id, 'Ты успешно купил ' + item + '!')
                                                                                            break

                                                                                        else:
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239097'

                                                                                            send(id, '😫Недостаточно средств! \n💰Баланс:'+ str(balance[id]))













                                                                                    elif msg == 'Назад':
                                                                                        keyboard = {"one_time": True, "buttons": list(range(0, len(cameras_rodnayaDerevnya) + 1))}
                                                
                                                                                        score = 0
                                                                                        for item in cameras_rodnayaDerevnya:
                                                                                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                                            score += 1

                                                                                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                        keyboard = str(keyboard.decode('utf-8'))

                                                                                        send(id, 'Вот все доступные вэбки:')
                                                                                        break




                                                                elif msg == 'Назад':
                                                                    photo = None
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Камеры"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                },
                                                                                {
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Микрофоны"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"

                                                                                }
                                                                            ]
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))
                                                                    send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')
                                                                    break



                                                                else:
                                                                    send(id, 'Дурак?')











                                            elif msg == 'Микрофоны':

                                                keyboard = {"one_time": True, "buttons": list(range(0, len(microphone_rodnayaDerevnya) + 1))}
                                                
                                                score = 0
                                                for item in microphone_rodnayaDerevnya:
                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                    score += 1

                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                send(id, 'Вот все доступные микрофоны:')

                                                for event in longpoll.listen():
                                                    await asyncio.sleep(0.5)
                                                    if time.time()-start >= 45:
                                                        if event.user_id != id:
                                                            send(event.user_id, '😕 попробуй ещё раз')
                                                        break
                                                    if event.type == VkEventType.MESSAGE_NEW:
                                                        if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                            msg = event.text
                                                            if id == event.user_id:
                                                                if msg in microphone_rodnayaDerevnya:
                                                                    item = msg
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Купить"
                                                                                    },
                                                                                    "color": "positive"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"
                                                                                }
                                                                            ]
                                                                                
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))

                                                                    send(id, 'Название: ' + msg + '\n Цена: ' + str(microphone_rodnayaDerevnya[msg]['cost']) + '\n усиление: ' + str(microphone_rodnayaDerevnya[msg]['gain']))
                                                                    
                                                                    for event in longpoll.listen():
                                                                        await asyncio.sleep(0.5)
                                                                        if time.time()-start >= 45:
                                                                            if event.user_id != id:
                                                                                send(event.user_id, '😕 попробуй ещё раз')
                                                                            break
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                                                msg = event.text
                                                                                if id == event.user_id:
                                                                                    if msg == 'Купить':
                                                                                        if balance[id] >= microphone_rodnayaDerevnya[item]['cost']:
                                                                                            inventory[id]['microphone']['name'] = item
                                                                                            inventory[id]['microphone']['cost'] = microphone_rodnayaDerevnya[item]['cost'] / 2
                                                                                            inventory[id]['microphone']['gain'] = microphone_rodnayaDerevnya[item]['gain']
                                                                                            inventory[id]['microphone']['photo'] = microphone_rodnayaDerevnya[item]['photo']
                                                                                            balance[id] -= microphone_rodnayaDerevnya[item]['cost']
                                                                                            
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239072%2Falbum-198179933_277009630'

                                                                                            send(id, 'Ты успешно купил ' + item + '!')
                                                                                            break


                                                                                        else:
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239097'

                                                                                            send(id, '😫Недостаточно средств! \n💰Баланс:'+ str(balance[id]))










                                                                                    elif msg == 'Назад':
                                                                                        keyboard = {"one_time": True, "buttons": list(range(0, len(microphone_rodnayaDerevnya) + 1))}
                                                
                                                                                        score = 0
                                                                                        for item in microphone_rodnayaDerevnya:
                                                                                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                                            score += 1

                                                                                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                        keyboard = str(keyboard.decode('utf-8'))

                                                                                        send(id, 'Вот все доступные вэбки:')
                                                                                        break




                                                                elif msg == 'Назад':
                                                                    photo = None
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Камеры"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                },
                                                                                {
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Микрофоны"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"

                                                                                }
                                                                            ]
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))
                                                                    send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')
                                                                    break



                                                                else:
                                                                    send(id, 'Дурак?')











                                            elif msg == 'Клавиатуры':

                                                keyboard = {"one_time": True, "buttons": list(range(0, len(keyboard_rodnayaDerevnya) + 1))}
                                                
                                                score = 0
                                                for item in keyboard_rodnayaDerevnya:
                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                    score += 1

                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                send(id, 'Вот все доступные микрофоны:')

                                                for event in longpoll.listen():
                                                    await asyncio.sleep(0.5)
                                                    if time.time()-start >= 45:
                                                        if event.user_id != id:
                                                            send(event.user_id, '😕 попробуй ещё раз')
                                                        break
                                                    if event.type == VkEventType.MESSAGE_NEW:
                                                        if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                            msg = event.text
                                                            if id == event.user_id:
                                                                if msg in keyboard_rodnayaDerevnya:
                                                                    item = msg
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Купить"
                                                                                    },
                                                                                    "color": "positive"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"
                                                                                }
                                                                            ]
                                                                                
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))

                                                                    send(id, 'Название: ' + msg + '\n Цена: ' + str(keyboard_rodnayaDerevnya[msg]['cost']) + '\n усиление: ' + str(keyboard_rodnayaDerevnya[msg]['gain']))
                                                                    
                                                                    for event in longpoll.listen():
                                                                        await asyncio.sleep(0.5)
                                                                        if time.time()-start >= 45:
                                                                            if event.user_id != id:
                                                                                send(event.user_id, '😕 попробуй ещё раз')
                                                                            break
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                                                msg = event.text
                                                                                if id == event.user_id:
                                                                                    if msg == 'Купить':
                                                                                        if balance[id] >= keyboard_rodnayaDerevnya[item]['cost']:
                                                                                            inventory[id]['keyboard']['name'] = item
                                                                                            inventory[id]['keyboard']['cost'] = keyboard_rodnayaDerevnya[item]['cost'] / 2
                                                                                            inventory[id]['keyboard']['gain'] = keyboard_rodnayaDerevnya[item]['gain']
                                                                                            inventory[id]['keyboard']['photo'] = keyboard_rodnayaDerevnya[item]['photo']
                                                                                            balance[id] -= keyboard_rodnayaDerevnya[item]['cost']
                                                                                            
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239072%2Falbum-198179933_277009630'

                                                                                            send(id, 'Ты успешно купил ' + item + '!')
                                                                                            break


                                                                                        else:
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239097'

                                                                                            send(id, '😫Недостаточно средств! \n💰Баланс:'+ str(balance[id]))












                                                                                    elif msg == 'Назад':
                                                                                        keyboard = {"one_time": True, "buttons": list(range(0, len(keyboard_rodnayaDerevnya) + 1))}
                                                
                                                                                        score = 0
                                                                                        for item in keyboard_rodnayaDerevnya:
                                                                                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                                            score += 1

                                                                                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                        keyboard = str(keyboard.decode('utf-8'))

                                                                                        send(id, 'Вот все доступные вэбки:')
                                                                                        break




                                                                elif msg == 'Назад':
                                                                    photo = None
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Камеры"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                },
                                                                                {
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Микрофоны"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"

                                                                                }
                                                                            ]
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))
                                                                    send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')
                                                                    break



                                                                else:
                                                                    send(id, 'Дурак?')









                                            elif msg == 'Мышки':

                                                keyboard = {"one_time": True, "buttons": list(range(0, len(mouse_rodnayaDerevnya) + 1))}
                                                
                                                score = 0
                                                for item in mouse_rodnayaDerevnya:
                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                    score += 1

                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                send(id, 'Вот все доступные мышки:')

                                                for event in longpoll.listen():
                                                    await asyncio.sleep(0.5)
                                                    if time.time()-start >= 45:
                                                        if event.user_id != id:
                                                            send(event.user_id, '😕 попробуй ещё раз')
                                                        break
                                                    if event.type == VkEventType.MESSAGE_NEW:
                                                        if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                            msg = event.text
                                                            if id == event.user_id:
                                                                if msg in mouse_rodnayaDerevnya:
                                                                    item = msg
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Купить"
                                                                                    },
                                                                                    "color": "positive"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"
                                                                                }
                                                                            ]
                                                                                
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))

                                                                    send(id, 'Название: ' + msg + '\n Цена: ' + str(mouse_rodnayaDerevnya[msg]['cost']) + '\n усиление: ' + str(mouse_rodnayaDerevnya[msg]['gain']))
                                                                    
                                                                    for event in longpoll.listen():
                                                                        await asyncio.sleep(0.5)
                                                                        if time.time()-start >= 45:
                                                                            if event.user_id != id:
                                                                                send(event.user_id, '😕 попробуй ещё раз')
                                                                            break
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                                                msg = event.text
                                                                                if id == event.user_id:
                                                                                    if msg == 'Купить':
                                                                                        if balance[id] >= mouse_rodnayaDerevnya[item]['cost']:
                                                                                            inventory[id]['mouse']['name'] = item
                                                                                            inventory[id]['mouse']['cost'] = mouse_rodnayaDerevnya[item]['cost'] / 2
                                                                                            inventory[id]['mouse']['gain'] = mouse_rodnayaDerevnya[item]['gain']
                                                                                            inventory[id]['mouse']['photo'] = mouse_rodnayaDerevnya[item]['photo']
                                                                                            balance[id] -= mouse_rodnayaDerevnya[item]['cost']
                                                                                            
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239072%2Falbum-198179933_277009630'

                                                                                            send(id, 'Ты успешно купил ' + item + '!')
                                                                                            break


                                                                                        else:
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239097'

                                                                                            send(id, '😫Недостаточно средств! \n💰Баланс:'+ str(balance[id]))












                                                                                    elif msg == 'Назад':
                                                                                        keyboard = {"one_time": True, "buttons": list(range(0, len(mouse_rodnayaDerevnya) + 1))}
                                                
                                                                                        score = 0
                                                                                        for item in mouse_rodnayaDerevnya:
                                                                                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                                            score += 1

                                                                                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                        keyboard = str(keyboard.decode('utf-8'))

                                                                                        send(id, 'Вот все доступные вэбки:')
                                                                                        break




                                                                elif msg == 'Назад':
                                                                    photo = None
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Камеры"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                },
                                                                                {
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Микрофоны"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"

                                                                                }
                                                                            ]
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))
                                                                    send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')
                                                                    break



                                                                else:
                                                                    send(id, 'Дурак?')








                                            elif msg == 'Мониторы':

                                                keyboard = {"one_time": True, "buttons": list(range(0, len(monitor_rodnayaDerevnya) + 1))}
                                                
                                                score = 0
                                                for item in monitor_rodnayaDerevnya:
                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                    score += 1

                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                keyboard = str(keyboard.decode('utf-8'))

                                                send(id, 'Вот все доступные мониторы:')

                                                for event in longpoll.listen():
                                                    await asyncio.sleep(0.5)
                                                    if time.time()-start >= 45:
                                                        if event.user_id != id:
                                                            send(event.user_id, '😕 попробуй ещё раз')
                                                        break
                                                    if event.type == VkEventType.MESSAGE_NEW:
                                                        if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                            msg = event.text
                                                            if id == event.user_id:
                                                                if msg in monitor_rodnayaDerevnya:
                                                                    item = msg
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Купить"
                                                                                    },
                                                                                    "color": "positive"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"
                                                                                }
                                                                            ]
                                                                                
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))

                                                                    send(id, 'Название: ' + msg + '\n Цена: ' + str(monitor_rodnayaDerevnya[msg]['cost']) + '\n усиление: ' + str(monitor_rodnayaDerevnya[msg]['gain']))
                                                                    
                                                                    for event in longpoll.listen():
                                                                        await asyncio.sleep(0.5)
                                                                        if time.time()-start >= 45:
                                                                            if event.user_id != id:
                                                                                send(event.user_id, '😕 попробуй ещё раз')
                                                                            break
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                                                msg = event.text
                                                                                if id == event.user_id:
                                                                                    if msg == 'Купить':
                                                                                        if balance[id] >= monitor_rodnayaDerevnya[item]['cost']:
                                                                                            inventory[id]['monitor']['name'] = item
                                                                                            inventory[id]['monitor']['cost'] = monitor_rodnayaDerevnya[item]['cost'] / 2
                                                                                            inventory[id]['monitor']['gain'] = monitor_rodnayaDerevnya[item]['gain']
                                                                                            inventory[id]['monitor']['photo'] = monitor_rodnayaDerevnya[item]['photo']
                                                                                            balance[id] -= monitor_rodnayaDerevnya[item]['cost']
                                                                                            
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239072%2Falbum-198179933_277009630'

                                                                                            send(id, 'Ты успешно купил ' + item + '!')
                                                                                            break


                                                                                        else:
                                                                                            keyboard = {
                                                                                                "one_time": True,
                                                                                                "buttons": [
                                                                                                    [{
                                                                                                            "action": {
                                                                                                                "type": "text",
                                                                                                                "label": "Назад"
                                                                                                            },
                                                                                                            "color": "primary"
                                                                                                        }
                                                                                                    ]
                                                                                                ]
                                                                                            }

                                                                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                            keyboard = str(keyboard.decode('utf-8'))

                                                                                            photo = 'photo-198179933_457239097'

                                                                                            send(id, '😫Недостаточно средств! \n💰Баланс:'+ str(balance[id]))












                                                                                    elif msg == 'Назад':
                                                                                        keyboard = {"one_time": True, "buttons": list(range(0, len(monitor_rodnayaDerevnya) + 1))}
                                                
                                                                                        score = 0
                                                                                        for item in monitor_rodnayaDerevnya:
                                                                                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                                            score += 1

                                                                                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                                        keyboard = str(keyboard.decode('utf-8'))

                                                                                        send(id, 'Вот все доступные вэбки:')
                                                                                        break




                                                                elif msg == 'Назад':
                                                                    photo = None
                                                                    keyboard = {
                                                                        "one_time": True,
                                                                        "buttons": [
                                                                            [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Камеры"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                },
                                                                                {
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Микрофоны"
                                                                                    },
                                                                                    "color": "secondary"
                                                                                }],
                                                                                [{
                                                                                    "action": {
                                                                                        "type": "text",
                                                                                        "label": "Назад"
                                                                                    },
                                                                                    "color": "primary"

                                                                                }
                                                                            ]
                                                                        ]
                                                                    }

                                                                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                    keyboard = str(keyboard.decode('utf-8'))
                                                                    send(id, 'Добро пожаловать в магазин Электротоваров!\nВыбирай что хочешь приобрести!')
                                                                    break



                                                                else:
                                                                    send(id, 'Дурак?')



                    


                        elif msg == 'Главное меню':
                            gm()

                            end = time.time()         
                            print(end-start) #Use then my code

                            break





                        else:
                            print('хз чо делать!!!!!!!!!111!1!!111')









async def two_maps():

    photo = None
                    
    if cities[id] == 'родная деревня':

        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": "Москва"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Питер"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Уфа"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Челябинск"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "родная деревня"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Назад"
                        },
                        "color": "negative"
                    }
                ]
            ]
        }

        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        send(id, random.choice(smiles) + random.choice(greetings) + ' ' + str(nicks[id]) + ', ты сейчас в  поселении "' + cities[id] + '! \n😈Выбирай куда поедем?')
    
    else:

        keyboard = {
            "one_time": True,
            "buttons": [
                [{
                        "action": {
                            "type": "text",
                            "label": "Москва"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Питер"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Уфа"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Челябинск"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "родная деревня"
                        },
                        "color": "secondary"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "label": "Назад"
                        },
                        "color": "negative"
                    }
                ]
            ]
        }

        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))

        send(id, random.choice(smiles) + random.choice(greetings) + ' ' + str(nicks[id]) + ', ты сейчас в  городе "' + cities[id] + '"! \n😈Выбирай куда поедем?')










async def workplace():

    photo = 'photo-198179933_457239076'

    keyboard = {
        "one_time": True,
        "buttons": [
            [{
                    "action": {
                        "type": "text",
                        "label": "Начать стрим"
                    },
                    "color": "secondary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "label": "Инвентарь"
                    },
                    "color": "secondary"
                }],
                [{
                    "action": {
                        "type": "text",
                        "label": "Главное меню"
                    },
                    "color": "primary"
                }
            ]
        ]
    }

    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    send(id, 'Добро пожаловать! это твое рабочее место. Здесь ты можешь творить или посмотреть свой инвентарь.')

    for event in longpoll.listen():
        await asyncio.sleep(0.5)
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                msg = event.text
                check = 1
                if id == event.user_id:
                    if msg == 'Начать стрим':
                        pass






                    elif msg == 'Инвентарь':
                        photo = None
                        keyboard = {"one_time": True, "buttons": list(range(0, len(inventory[id]) + 1))}
                        score = 0
                        for item in inventory[id]:
                            keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                            score += 1

                        keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                        keyboard = str(keyboard.decode('utf-8'))
                        send(id, 'Вот список всего того, что у тебя есть:')
                        
                        for event in longpoll.listen():
                            await asyncio.sleep(0.5)
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                    msg = event.text
                                    check = 1
                                    if id == event.user_id:
                                        if msg in list(inventory[id]):
                                            item = msg
                                            photo = inventory[id][item]['photo']
                                            keyboard = {
                                                "one_time": True,
                                                "buttons": [
                                                    [{
                                                            "action": {
                                                                "type": "text",
                                                                "label": "продать"
                                                            },
                                                            "color": "secondary"
                                                        }],
                                                        [{
                                                            "action": {
                                                                "type": "text",
                                                                "label": "Назад"
                                                            },
                                                            "color": "primary"
                                                        }
                                                    ]
                                                ]
                                            }

                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                            keyboard = str(keyboard.decode('utf-8'))

                                            send(id, 'Вот характеристики твоего ' + inventory[id][item]['name'] + ':\nЦена - ' + str(inventory[id][item]['cost'])+ '\nУсиление - ' + str(inventory[id][item]['gain']))

                                            for event in longpoll.listen():
                                                await asyncio.sleep(0.5)
                                                if event.type == VkEventType.MESSAGE_NEW:
                                                    if event.from_user and not (event.from_me): # если сообщение НЕ от бота
                                                        msg = event.text
                                                        check = 1
                                                        if id == event.user_id:
                                                            if msg == 'продать':
                                                                photo = 'photo-198179933_457239077'

                                                                keyboard = {
                                                                    "one_time": True,
                                                                    "buttons": [
                                                                        [{
                                                                                "action": {
                                                                                    "type": "text",
                                                                                    "label": "Назад"
                                                                                },
                                                                                "color": "primary"
                                                                            }
                                                                        ]
                                                                    ]
                                                                }

                                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                keyboard = str(keyboard.decode('utf-8'))

                                                                balance[id] += inventory[id][item]['cost']
                                                                inventory[id][item]['cost'] = 0
                                                                inventory[id][item]['gain'] = 0
                                                                inventory[id][item]['photo'] = None

                                                                send(id, 'Ты успешно продал ' + inventory[id][item]['name'])
                                                                
                                                                inventory[id][item]['name'] = 'Ничего'



                                                            elif msg == 'Назад':
                                                                photo = None
                                                                keyboard = {"one_time": True, "buttons": list(range(0, len(inventory[id]) + 1))}
                                                                score = 0
                                                                for item in inventory[id]:
                                                                    keyboard["buttons"][score] = [{"action": {"type": "text","label": item},"color": "secondary"}]
                                                                    score += 1

                                                                keyboard["buttons"][score] = [{"action": {"type": "text","label": "Назад"},"color": "primary"}]

                                                                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                                                keyboard = str(keyboard.decode('utf-8'))
                                                                send(id, 'Вот список всего того, что у тебя есть:')
                                                                break



                                        elif msg == 'Назад':
                                            photo = 'photo-198179933_457239076'

                                            keyboard = {
                                                "one_time": True,
                                                "buttons": [
                                                    [{
                                                            "action": {
                                                                "type": "text",
                                                                "label": "Начать стрим"
                                                            },
                                                            "color": "secondary"
                                                        }],
                                                        [{
                                                            "action": {
                                                                "type": "text",
                                                                "label": "Инвентарь"
                                                            },
                                                            "color": "secondary"
                                                        }],
                                                        [{
                                                            "action": {
                                                                "type": "text",
                                                                "label": "Главное меню"
                                                            },
                                                            "color": "primary"
                                                        }
                                                    ]
                                                ]
                                            }

                                            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                                            keyboard = str(keyboard.decode('utf-8'))

                                            send(id, 'Добро пожаловать! это твое рабочее место. Здесь ты можешь творить или посмотреть свой инвентарь.')
                                            break







                    elif msg == 'Главное меню':
                        gm()
                        break








# ``````````````````````````````````````````````````````````````````````````````````````````````````````













# ``````````````````````````````ВЫГРУЗКА ВСЕХ ПЕРЕМЕННЫХ```````````````````````````````````````````````````````

# выгрузка переменной "баланс" (balance)
file = open(str("balance.txt"), "r", encoding='utf-8')
balance = eval(file.read())
file.close()

    
# выгрузка переменной "ники" (nicks)
file = open(str("nicks.txt"), "r", encoding='utf-8')
nicks = eval(file.read())
file.close()


# выгрузка переменной "админы" (admins)
file = open("admins.txt", "r", encoding='utf-8')
admins = eval(file.read())
file.close()


# выгрузка переменной "дома" (houses)
file = open("houses.txt", "r", encoding='utf-8')
houses = eval(file.read())
file.close()


# выгрузка переменной "чек_старт" (check_start)
file = open('check_start.txt', 'r', encoding='utf-8')
check_start = eval(file.read())
file.close()


# выгрузка переменной "города" (cities)
file = open('cities.txt', 'r', encoding='utf-8')
cities = eval(file.read())
file.close()

# выгрузка переменной "инвентарь" (inventory)
file = open(str("inventory.txt"), "r", encoding='utf-8')
inventory = eval(file.read())
file.close()

# `````````````````````````````````````````````````````````````````````````````````````````````










# ````````````````````````````ОСНОВНАЯ РАБОТА БОТА```````````````````````````````````````````````````````

async def main():

    # Слушаем лонгпул (события в боте)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW: # Если пришло новое сообщение

            msg = event.text.lower() # сообщение это...
            id = event.user_id #айди пользователя

            #try:

            if event.from_user and not (event.from_me): # если сообщение НЕ от бота


                if msg[0:10] == 'переверни ':
                    rotateText(msg)


                elif msg[: 9] == 'переведи ':
                    translateText(msg[9:])

   
                elif msg == 'начать':
                    main_loop.create_task(starting())

                
                elif msg == 'главное меню' or msg == 'гм':
                    main_loop.create_task(gm())


                elif msg == 'магазин':
                    main_loop.create_task(shop())


                elif msg == 'дубль карты':
                    main_loop.create_task(two_maps())


                elif msg == 'рабочее место':
                    main_loop.create_task(workplace())


                elif msg[ : 9] == 'рассылка ':
                    mailing(msg)


                elif msg == 'стоп':
                    break

                else:
                    send(id, 'Напиши "помощь", чтобы узнать мои команды')


            save("balance.txt", balance)
            save("nicks.txt", nicks)
            save("admins.txt", admins)
            save("houses.txt", houses)
            save("check_start.txt", check_start)
            save("cities.txt", cities)
            save("inventory.txt", inventory)



            """except Exception as e:
                photo = None
                send(id_admin, 'Хэй! я тут у [id' + str(id) + '|игрока] ошибку словил! Она звучит так: \n' + str(e))
                send(id, "Хмм... Ошибка при работе. Не волнуйся, я уже написал об этом админу.")"""




main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())



#asyncio.run(main())
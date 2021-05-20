from bot import bot
from bot import server
from keyboards import testKeys
from view import get_sites


@bot.message_handler(commands=['start'])
def start_message(message):
    print("Start")
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=testKeys)


@bot.message_handler(content_types=['photo'])
def send_photo(message):
    print(message)
    file_id = message.photo[-1].file_id
    print("file id:", file_id)
    file = bot.get_file(file_id)
    print("file:", file)

    try:
        file_path = file.file_path
        print("file path:", file_path)
    except Exception as e:
        print("get file path error:")
        print("\t", e)


@bot.message_handler(content_types=['text'])
def send_text(message):
    code, resp = server.send_message(message.from_user.id, message.text)

    print(message.from_user.id, end=' \t:: ')
    print(message.text)

    print("code: ", code)
    print("resp: ", resp)

    print("-----------------------")
    if code == 200:
        bot.send_message(message.chat.id, resp['next_message'])
    else:
        bot.send_message(message.chat.id, 'неизвестная ошибка сервера')




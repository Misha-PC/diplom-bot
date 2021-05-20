import telebot


testKeys = telebot.types.ReplyKeyboardMarkup()
testKeys.row('Привет', 'Пока')

mainKeys = telebot.types.ReplyKeyboardMarkup()
mainKeys.row('Мои сайты', 'Создать новый', 'Тарифы')


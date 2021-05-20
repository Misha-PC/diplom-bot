from bot import bot
import handlers

# from database import Database
# db = Database('static/db.ini')

# db.add_site(
#     member_id=123321,
#     title="auto-gen",
#     head="It is auto generated site!",
#     side_bar=['Проверка', 'русского', 'текста']
# )

# s = db.get_sites(id_=8)
# for i in s:
#     print(i)
# print("--------\n{}\n--------".format(len(s)))
# print("--------\n{}\n--------".format(s))
bot.polling()






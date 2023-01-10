import os
import threading
import sqlite3


import telebot, time
from bd import *
from cat_recognizer import CatRecognizer
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))
bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
get_connect()
def download_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    dest = str(threading.get_ident())
    with open(dest, 'wb') as new_file:
        new_file.write(downloaded_file)
    return dest


class AlwaysFalseRecognizer(CatRecognizer):
    def is_cat(self, image_path: str) -> bool:
        return False

cat_recognizer = AlwaysFalseRecognizer()

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_name = download_photo(message)
    print(file_name)
    tg_file_id = file_name
    user_id = message.from_user.id
    is_cat = message.from_user.is_bot
    uploaded_at = tconv(message.date)
    print (message.from_user.id)
    print (message.from_user.is_bot)
    print (tconv(message.date))
    print (message.from_user)
    max_id = get_max_id()
    print(max_id)
    insert_data(max_id+1,tg_file_id, user_id, is_cat, uploaded_at)
    bot.send_message(message.chat.id, cat_recognizer.is_cat(file_name))
    os.remove(file_name)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello\nWhat do you want to do?\n'
                                      '- /statistics\n'
                                      '- /help</b>', parse_mode = 'html')




@bot.message_handler(commands=['statistics'])
def statistics(message):
    bot.send_message(message.chat.id, '<b>You haven\'t sent a photo yet</b>', parse_mode = 'html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, open('help_cmd_text.txt', 'r', -1, 'utf-8').read(), parse_mode ='html')

@bot.message_handler()
def all(message):
    if message.text == 'hi':
        mess = f'Hello, <b>{message.from_user.first_name} </b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'info':
        mess = {message.from_user}
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Please, choose another command: \nhi\ninfo')

bot.polling(none_stop = True)
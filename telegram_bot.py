import os
import threading
import sqlite3

from main_cat_recognizer import CATorNOT
import telebot, time
from bd import *
# from cat_recognizer import CatRecognizer
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))
bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
get_connect()
def download_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    dest = str(threading.get_ident())
    with open(dest, 'wb') as new_file:
        new_file.write(downloaded_file)
    return dest


# class AlwaysFalseRecognizer(CatRecognizer):
#     def is_cat(self, image_path: str) -> bool:
#         return False
#
# cat_recognizer = AlwaysFalseRecognizer()

def get_user_id(message):
    return message.from_user.id

def take_and_insert_variables(message, file_name):
    tg_file_id = file_name
    user_id = get_user_id(message)
    is_cat = CATorNOT(tg_file_id)
    uploaded_at = tconv(message.date)
    # max_id = get_max_id(user_id)
    insert_data(tg_file_id, user_id, is_cat, uploaded_at)
    return is_cat

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_name = download_photo(message)
    is_cat = take_and_insert_variables(message, file_name)
    bot.send_message(message.chat.id, is_cat)
    os.remove(file_name)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello\nWhat do you want to do?\n'
                                      '- /statistics\n'
                                      '- /help</b>', parse_mode = 'html')




@bot.message_handler(commands=['statistics'])
def statistics(message):
    bot.send_message(message.chat.id, '<b>You haven\'t \n'
                                      '- /Count_cats\n'
                                      '- /Count_NotCats\n'
                                      '- /Count_sent_photos\n'
                                      '- /My_id</b>', parse_mode = 'html')

@bot.message_handler(commands = ['My_id'])
def my_id(message):
    bot.send_message(message.chat.id, get_user_id(message))

@bot.message_handler(commands = ['Count_cats'])
def count_cats(message):
    user_id = get_user_id(message)
    sum = true_answers(user_id)
    bot.send_message(message.chat.id, 'You sent '+ '<b>'+str(sum)+'</b>'+' photos with Cats', parse_mode = 'html')

@bot.message_handler(commands = ['Count_NotCats'])
def count_not_cats(message):
    user_id = get_user_id(message)
    sum = false_answers(user_id)
    bot.send_message(message.chat.id, 'You sent '+ '<b>'+str(sum)+'</b>'+' photos where no Cats', parse_mode = 'html')

@bot.message_handler(commands = ['Count_sent_photos'])
def count_all_cats(message):
    user_id = get_user_id(message)
    sum = all_photos(user_id)
    bot.send_message(message.chat.id, 'You sent '+ '<b>'+str(sum)+'</b>'+' of all the time', parse_mode = 'html')

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
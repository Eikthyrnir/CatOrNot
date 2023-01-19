import os
import threading
from keras_cat_recognizer import KerasCatRecognizer
import telebot, time
from bd import *

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


def message_time_as_str(message):
    str_time = time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(message))
    return str_time


def get_user_id(message):
    return message.from_user.id


def save_img_recognition_results(message, is_cat):
    tg_file_id = message.photo[-1].file_id
    user_id = get_user_id(message)
    uploaded_at = message_time_as_str(message.date)
    insert_data(tg_file_id, user_id, is_cat, uploaded_at)


recognition_answers = {True: 'Cat',
                       False: 'Not a cat'}

cat_recognizer = KerasCatRecognizer()


@bot.message_handler(content_types=['photo'])
def photo(message):
    file_name = download_photo(message)
    is_cat = cat_recognizer.is_cat(file_name)
    save_img_recognition_results(message, is_cat)
    bot.send_message(message.chat.id, recognition_answers[is_cat])
    os.remove(file_name)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello\nWhat do you want to do?\n'
                                      '- /statistics\n'
                                      '- /help</b>', parse_mode='html')


@bot.message_handler(commands=['statistics'])
def statistics(message):
    user_id = get_user_id(message)
    all = all_photos(user_id)
    if all == 0:
        bot.send_message(message.chat.id, '<b>📈 Statistics:\nYou haven\'t sent any images yet \n</b>', parse_mode='html')
        return

    cats = true_answers(user_id)
    bot.send_message(message.chat.id, '<b>📈 Statistics:\nYou have already sent ' + str(all) + ' images\n'
                                      'Cats number: ' + str(cats) + '\n'
                                      'Cats percentage: ' + str((cats / all) * 100) + '\n</b>', parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, open('help_cmd_text.txt', 'r', -1, 'utf-8').read(), parse_mode='html')


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


bot.polling(none_stop=True)

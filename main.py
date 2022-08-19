import telebot
import glob
import random
from telebot import types
from random import choice
import os
from spiski import spis, spis1

f = open('G:\comp.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('G:\\anime.txt', 'r', encoding='UTF-8')
anime = f.read().split('\n')
f.close()

f = open('G:\\ekshen.txt', 'r', encoding='UTF-8')
ekshen = f.read().split('\n')
f.close()

f = open('G:\\drama.txt', 'r', encoding='UTF-8')
drama = f.read().split('\n')
f.close()

f = open('G:\\romantika.txt', 'r', encoding='UTF-8')
romantika = f.read().split('\n')
f.close()

token = 'your token'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", 'stop'])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("комплимент")
        item2=types.KeyboardButton("фото")
        item3 = types.KeyboardButton("картинка")
        item4 = types.KeyboardButton("посоветовать аниме")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(m.chat.id, 'привет',  reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'комплимент' :
            print('комплимент')
            answer = random.choice(facts)
            bot.send_message(message.chat.id, answer)

    elif message.text.strip() == 'фото':
            print('фото')
            bot.send_photo(message.chat.id, photo = open(random.choice(spis), 'rb'))

    elif message.text.strip() == 'картинка':
        milo = random.choice(spis1)
        bot.send_photo(message.chat.id, photo=open(milo, 'rb'))

    elif message.text.strip() == 'посоветовать аниме' :
            print('посоветовать аниме')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'какой жанр аниме посоветовать?)')
            item1 = types.KeyboardButton("экшен")
            item2 = types.KeyboardButton("романтика")
            item3 = types.KeyboardButton("драма")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(back)
            bot.send_message(message.chat.id, 'выбирайте)',reply_markup=markup)

    elif message.text == 'экшен':
            answer1 = random.choice(ekshen)
            bot.send_message(message.chat.id, answer1)

    elif message.text == 'драма' :
            answer1 = random.choice(drama)
            bot.send_message(message.chat.id, answer1)

    elif message.text == 'романтика' :
            answer1 = random.choice(romantika)
            bot.send_message(message.chat.id, answer1)

    elif message.text == 'Вернуться в главное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("комплимент")
            item2 = types.KeyboardButton("фото")
            item3 = types.KeyboardButton("картинка")
            item4 = types.KeyboardButton("посоветовать аниме")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            bot.send_message(message.chat.id, text="вы в главном меню))", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'такой функции не существует')


bot.polling(none_stop=True, interval=0)
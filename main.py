import requests
from bs4 import BeautifulSoup
import random
import telebot

URL = ''
token = '5477951265:AAE2xH6di6GRP5EsoZAIZ_X4yo1LtQzhSlM'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Вот, что я могу:')
    bot.send_message(message.chat.id, '1. КНБ - сыграть в камень ножницы бумага. \nПравила игры: '
                                      'Бумага побеждает камень. '
                                      'Камень побеждает ножницы. '
                                      'Ножницы побеждают бумагу.')
    bot.send_message(message.chat.id, '2. Виселица - сыграть виселица. \nПравила игры: '
                                      'Я загадываю слово, вместо букв пишу * и рисую основание виселицы, '
                                      'когда называете неправильную букву я пририсовываю еще часть'
                                      'Вы пытаетесь угадать это слово. (буквы ё там быть не может)')
    bot.send_message(message.chat.id, '3. Змейка - сыграть в змейку.')
    bot.send_message(message.chat.id, '4. Валюты - конвертация из одной валюты в другую.')
    bot.send_message(message.chat.id, '5. Монетка - подкинуть монетку.')
    bot.send_message(message.chat.id, '6. Ипотека - ипотечный калькулятор.')
    bot.send_message(message.chat.id, '7. Даты - калькулятор дат.')


@bot.message_handler(content_types=['text'])
def command(message):
    if message.text.lower() == 'кнб':
        bot.send_message(message.chat.id, 'Напишите камень, ножницы или бумага')
        rock_paper_scissors()
    elif message.text.lower() == 'виселица':
        bot.send_message(message.chat.id, '')
        hangman()
    elif message.text.lower() == 'даты':
        bot.send_message(message.chat.id, 'Напишите две даты')
    elif message.text.lower() == 'валюты':
        bot.send_message(message.chat.id, 'Напишите валюту, затем сумму. '
                                          'Следующим сообщением - валюту, в которую переводим.')
    elif message.text.lower() == 'монетка':
        bot.send_message(message.chat.id, random.SystemRandom().choice(["Орёл", "Решка"]))
    elif message.text.lower() == 'ипотека':
        bot.send_message(message.chat.id, '')
    else:
        bot.send_message(message.chat.id, 'Я Вас не понимаю.')


@bot.message_handler(content_types=['text'])
def rock_paper_scissors(message):
    bots_choosing = random.SystemRandom().choice(['Камень', 'Ножницы', 'Бумага'])
    bot.send_message(message.chat.id, bots_choosing)
    bots_choosing = bots_choosing.lower()
    if message.text.lower() == bots_choosing:
        bot.send_message(message.chat.id, 'Ничья!')
    elif (message.text.lower() == 'камень' and bots_choosing == 'ножницы') or \
            (message.text.lower() == 'ножницы' and bots_choosing == 'бумага') or \
            (message.text.lower() == 'бумага' and bots_choosing == 'камень'):
        bot.send_message(message.chat.id, 'Вы победитель!')
    else:
        bot.send_message(message.chat.id, 'Вы проиграли :(')


def hangman():
    with open("Слова для виселицы.txt", "r") as file:
        text = file.read()
    words = list(map(str, text.split()))
    word = random.choice(words)
    guessing_word = '*' * len(word)
    pics = []


bot.polling()

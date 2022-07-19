import requests

import telebot 

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "This bot returns the description of the chosen Pokemon. To choose a Pokemon, enter its name")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{message.text.lower()}')
        toJson = pokemon.json()
        secondCall = requests.get(toJson['species']['url'])
        secondToJson = secondCall.json()
        data = secondToJson['flavor_text_entries'][0]['flavor_text']
        newData= ''
        for l in data:
            if l == '\n':
                l = ' '
            newData = newData + l
        bot.reply_to(message, newData)
    except:
        bot.reply_to(message, 'The selected Pokemon was not found. This can be due to it does not exist or its not currently available on our database.')
bot.polling()

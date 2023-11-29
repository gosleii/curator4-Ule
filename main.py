import telebot

bot = telebot.TeleBot('5838664189:AAHNOOGpWUQOprAaxRqu5SIHuEf7b_0RlRA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Доброго времени суток!")


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Чем я могу помочь? \nУкажите проблему")


bot.infinity_polling()

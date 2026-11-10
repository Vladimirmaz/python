import telebot

# Вставьте сюда токен, полученный от @BotFather
TOKEN = '8729105792:AAHKUlshH25xsTmwigTRdVFz6Khoa6AhBJo'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, 'Привет!')


# Запуск постоянного опроса серверов Telegram
bot.infinity_polling()

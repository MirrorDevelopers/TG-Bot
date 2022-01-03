import os
import telebot


bot = telebot.TeleBot("5088301449:AAEYbFdLo1iZwg7tfNDxHM1cbrNojA-drCE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Garry.")

@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/AnyStudent")



bot.polling()

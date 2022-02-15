import os
import telebot


bot = telebot.TeleBot("5088301449:AAEYbFdLo1iZwg7tfNDxHM1cbrNojA-drCE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Garry.")

@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "Oh Wanna Be A Team Member.Send Your Name,Username,Verification (required),Performance Of :- eg:Pyrogram, Making Par")

@bot.message_handler(commands=["offers"])
def send_message(message):
  bot.send_message(message.chat.id, "Aztre Free Shipping For Asian Countries Use Promo Code TheShadowPro 50% Off Valid Till February 16 2024")


bot.polling()

import os
import telebot


bot = telebot.TeleBot("5088301449:AAEYbFdLo1iZwg7tfNDxHM1cbrNojA-drCE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Garry.[supunma <sz/>](https://t.me/szteambots)")
BUTTONS = ( [ [ InlineKeyboardButton( text="🆘 Help 🆘", callback_data = "helpmenu_" ), InlineKeyboardButton( text="📊 Stats 📊", callback_data="stats_callback", ), ], [ InlineKeyboardButton( text="🗣 Updates", url="https://t.me/szteambots" ), InlineKeyboardButton( text="👥 Support", url="https://t.me/slbotzone", ), ], [ InlineKeyboardButton( text="➕ Add Me To Your Group ➕", url=f"t.me/szrosebot?startgroup=true", ) ], ])


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/AnyStudent")



bot.polling()

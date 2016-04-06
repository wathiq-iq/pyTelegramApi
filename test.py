# -*- coding: utf-8 -*-
"""
Code By: W3thiq 
""" 
import telebot
import api

bot = telebot.TeleBot(api.Token)


@bot.message_handler(content_types=['text'])
def handle_text(message):
  bot.send_message(message.from_user.id,"""\r
  *Bold*
  _italic_
  `code`
  ```coder```
  [TEXT](ULR)""", parse_mode="Markdown")
  
bot.polling(none_stop=True)
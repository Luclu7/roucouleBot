# coding=UTF-8

import os
import telebot
  
bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO) # Outputs debug messages to console.

@bot.message_handler(func=lambda message: "achet" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "pigeon")

@bot.message_handler(func=lambda message: "préco" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "pigeon")

@bot.message_handler(func=lambda message: "preco" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "pigeon")

@bot.message_handler(func=lambda message: "achèt" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "pigeon")

@bot.message_handler(func=lambda message: "acha" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "pigeon")

@bot.message_handler(func=lambda message: "tg" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "v")

@bot.message_handler(func=lambda message: "pn" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "l")

@bot.message_handler(func=lambda message: "sfr" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "SLURP SFR NYO MEILLEUR 4G DE FRANCE OMG")

@bot.message_handler(func=lambda message: "test" in message.text.lower())
def command_text(m):
	bot.send_message(m.chat.id, "reçu")

bot.polling()
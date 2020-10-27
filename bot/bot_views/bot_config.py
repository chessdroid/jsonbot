import telebot
from django.conf import settings	
from telebot import apihelper
import json
from django.template.loader import render_to_string
from bot.models import Account

apihelper.ENABLE_MIDDLEWARE = True
bot = telebot.TeleBot(settings.TOKEN, parse_mode="HTML") 


@bot.middleware_handler(update_types=['message'])
def modify_message(bot_instance, message):
	
	message.update_id = bot_instance.last_update_id
	message.json["update_id"]= bot_instance.last_update_id


@bot.message_handler()
def handler(message):	
	message_dict =  dict(message.json)
	resp=render_to_string( "format.html", message_dict)
	bot.send_message(message.from_user.id,	resp)
	obj, created = Account.objects.update_or_create(message_dict['from'])

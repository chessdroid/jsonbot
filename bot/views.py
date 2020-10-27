import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .bot_views.bot_config import bot


@csrf_exempt
def update(request):	
	if request.method=="POST":
		json_string = request.body.decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])

	return HttpResponse('')

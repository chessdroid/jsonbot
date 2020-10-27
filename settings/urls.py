from django.contrib import admin
from django.urls import path
from bot.views import update

urlpatterns = [
    path('', admin.site.urls),
    path('get_updates/', update),
]

from django.urls import path
from .views import user_profile
from .views import dietitian_bot, trainer_bot

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('dietitian/', dietitian_bot, name='dietitian_bot'),
    path('trainer/', trainer_bot, name='trainer_bot'),
]

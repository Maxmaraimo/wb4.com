from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('wb4pay/', wb4pay, name='wb4pay'),
    path('video/', video, name='video'),
    path('support/', support, name='support'),
    path('stickers/', stickers, name='stickers'),
    path('services/', services, name='services'),
    path('photos/', photos, name='photos'),
    path('news/', news, name='news'),
    path('music/', music, name='music'),
    path('message/', message, name='message'),
    path('markett/', markett, name='markett'),
    path('groups/', groups, name='groups'),
    path('game/', game, name='game'),
    path('clips/', clips, name='clips'),
    path('calls/', calls, name='calls'),
    path('friends/', friends, name='friends')

]
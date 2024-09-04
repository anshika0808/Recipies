from django.urls import path
from home.views import *


urlpatterns = [
    path('',home , name="home"),
    path('about/',about,name='about'),
    path('success_page/',success,name='success'),
    path('contact/',contact,name='contact'),
    path('registration/',registration , name="registration"),
    path('login/',login,name='login'),
    path('logout/',logout_page,name='logout_page'),
]

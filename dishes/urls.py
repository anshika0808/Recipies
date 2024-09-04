from django.urls import path
from dishes.views import *


urlpatterns = [
    path('',recipie , name="recipie"),
    path('vege/',vege,name='vege'),
    path('Delete_dish/<int:id>/',Delete_dish,name='Delete_dish'),
    path('update_dish/<int:id>/',update_dish,name='update_dish'),
]
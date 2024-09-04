from django.db import models

# Create your models here.
class Dishes(models.Model):
    dish_name=models.CharField(max_length=100)
    dish_desc=models.TextField()
    dish_image=models.ImageField(upload_to='recipie')

    def __str__(self):
        return self.dish_name
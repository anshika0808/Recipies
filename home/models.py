from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    Email=models.EmailField()
    address=models.TextField()
    
    def __str__(self):
        return self.name
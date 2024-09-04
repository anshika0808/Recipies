# Generated by Django 5.0.7 on 2024-07-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_desc', models.TextField()),
                ('dish_image', models.ImageField(upload_to='recipie/')),
            ],
        ),
    ]

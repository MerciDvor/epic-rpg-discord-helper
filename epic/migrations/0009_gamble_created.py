# Generated by Django 3.1.3 on 2020-11-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic', '0008_gamble'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamble',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 2.2.17 on 2020-12-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotinder', '0010_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_type',
            field=models.CharField(choices=[('Компания', 'Компания'), ('Фонд', 'Фонд'), ('Частный', 'Частный')], default='Компания', max_length=20),
        ),
    ]

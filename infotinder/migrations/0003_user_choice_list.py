# Generated by Django 2.2.17 on 2020-12-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infotinder", "0002_auto_20201201_1518"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="choice_list",
            field=models.ManyToManyField(through="infotinder.Choicelist", to="infotinder.Startapp"),
        ),
    ]

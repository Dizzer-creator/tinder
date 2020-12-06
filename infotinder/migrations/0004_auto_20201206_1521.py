# Generated by Django 2.2.17 on 2020-12-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infotinder", "0003_user_choice_list"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ptinder",
            new_name="PageTinder",
        ),
        migrations.RenameModel(
            old_name="Startapp",
            new_name="StartUp",
        ),
        migrations.AlterField(
            model_name="user",
            name="choice_list",
            field=models.ManyToManyField(through="infotinder.ChoiceList", to="infotinder.StartUp"),
        ),
    ]

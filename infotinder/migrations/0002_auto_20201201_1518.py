# Generated by Django 2.2.17 on 2020-12-01 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("infotinder", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="list_no",
        ),
        migrations.RemoveField(
            model_name="user",
            name="list_yes",
        ),
        migrations.RemoveField(
            model_name="user",
            name="type_company",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_or_investor",
        ),
        migrations.CreateModel(
            name="Choicelist",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("choice_type", models.BooleanField(default=False)),
                ("startapp", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="infotinder.Startapp")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

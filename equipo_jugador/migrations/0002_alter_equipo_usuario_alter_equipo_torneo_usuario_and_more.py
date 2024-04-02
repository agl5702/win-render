# Generated by Django 4.2.7 on 2024-04-02 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("equipo_jugador", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipo",
            name="usuario",
            field=models.ForeignKey(
                default=users.models.UserManager.get_default_user,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="equipo_torneo",
            name="usuario",
            field=models.ForeignKey(
                default=users.models.UserManager.get_default_user,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="jugador",
            name="usuario",
            field=models.ForeignKey(
                default=users.models.UserManager.get_default_user,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-28 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_rename_wiadomosc_czat_czat_czat_stworzono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='czat',
            name='uzytkownik',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

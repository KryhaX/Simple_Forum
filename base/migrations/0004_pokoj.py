# Generated by Django 4.2.5 on 2023-09-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_moje_konto_delete_rejestracja_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokoj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=70)),
                ('opis', models.TextField(blank=True, null=True)),
                ('aktualizacja', models.DateTimeField(auto_now=True)),
                ('stworzono', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

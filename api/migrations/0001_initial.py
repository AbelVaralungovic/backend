# Generated by Django 5.0.2 on 2024-02-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objava',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=50)),
                ('sadrzaj', models.TextField()),
                ('kreirano', models.TimeField(auto_now_add=True)),
                ('azurirano', models.TimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-22 13:06

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_objava_slika'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objava',
            options={'ordering': ['-kreirano']},
        ),
        migrations.AddField(
            model_name='objava',
            name='pisac',
            field=models.ForeignKey(default=api.models.get_default_pisac, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='objava',
            name='slika',
            field=models.ImageField(default='/images/default.jpg', upload_to='images/'),
        ),
    ]
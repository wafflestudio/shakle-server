# Generated by Django 3.2.6 on 2022-09-14 17:02

from django.db import migrations, models
import sharkle.upload_image


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220702_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(null=True, upload_to=sharkle.upload_image.upload_image),
        ),
    ]
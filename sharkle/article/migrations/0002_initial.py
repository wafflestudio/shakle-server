# Generated by Django 3.2.6 on 2022-02-24 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='board.board'),
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
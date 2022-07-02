# Generated by Django 3.2.6 on 2022-07-01 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circle', '0003_alter_circle_make_new_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=100)),
                ('highlight', models.BooleanField(default=False)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='circle.circle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailconfirm',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regulations',
            name='terms_and_conditions',
        ),
        migrations.AddField(
            model_name='register_model',
            name='terms_and_conditions',
            field=models.BooleanField(default=False),
        ),
    ]
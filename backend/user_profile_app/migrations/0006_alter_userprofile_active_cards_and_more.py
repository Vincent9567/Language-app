# Generated by Django 5.0.6 on 2024-06-08 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile_app', '0005_alter_userprofile_words_learned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='active_cards',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='words_learned',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

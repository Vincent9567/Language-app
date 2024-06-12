# Generated by Django 5.0.6 on 2024-06-08 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flashcard_app', '0001_initial'),
        ('target_language_app', '0001_initial'),
        ('user_profile_app', '0006_alter_userprofile_active_cards_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='target_language_app.targetlanguage'),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='user_id',
            field=models.ManyToManyField(to='user_profile_app.userprofile'),
        ),
    ]

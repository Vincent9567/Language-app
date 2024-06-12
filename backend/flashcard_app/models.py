from django.db import models
from django.core import validators as v
from .validators import validate_word
from target_language_app.models import TargetLanguage
from user_profile_app.models import UserProfile



class FlashCard(models.Model):

    language_id = models.ForeignKey(TargetLanguage, on_delete = models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    foreign_word = models.CharField(validators=[validate_word])
    native_translation = models.CharField(validators=[validate_word])
    times_seen = models.IntegerField(default=0, validators=[v.MinValueValidator(0)])
    difficulty_rating = models.IntegerField(default=10, validators=[v.MinValueValidator(0)])

    def __str__(self) -> str:

        return f'Foreign word: {self.foreign_word},\
                 Translation: {self.native_translation},\
                 Times seen: {self.times_seen},\
                 Difficulty: {self.difficulty_rating}'
    
    def change_difficulty_rating(self, new_rating):
        self.difficulty_rating = new_rating
        self.save()

    def increase_times_seen(self):
        self.times_seen += 1
        self.save()
                 
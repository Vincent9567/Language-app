from django.db import models
from django.core import validators as v
from .validators import validate_name
from target_language_app.models import TargetLanguage

# Create your models here.


class UserProfile(models.Model):

    user_name = models.CharField(max_length=255, unique = True, blank = False, validators=[validate_name])
    user_email = models.EmailField(unique = True, blank= False)
    target_language_id = models.ForeignKey(TargetLanguage, on_delete=models.CASCADE, null=True)
    target_language = models.CharField(max_length=255)
    native_language = models.CharField(max_length=255, blank= False, default='English')
    active_cards = models.IntegerField(default=0, validators=[v.MinValueValidator(0), v.MaxValueValidator(50)])
    words_learned = models.IntegerField(default=0, validators=[v.MinValueValidator(0)])

    def __str__(self) -> str:
        return f'Username: {self.user_name}, Email: {self.user_email}, Target Language: {self.target_language}'
    

    def add_active_card(self, total_cards):
        self.active_cards += total_cards
        self.save()

    def add_words_learned(self, words_learned):
        self.words_learned += words_learned
        self.save()
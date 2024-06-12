from django.db import models

# Create your models here.

class TargetLanguage(models.Model):

    language_name = models.CharField(blank=False, default='Spanish', unique=True)
    flag_string_url = models.CharField(blank=True, null=True)


    def __str__(self) -> str:
        return f'Language: {self.language_name}'
    

    def add_flag_string(self, string):
        self.flag_string_url = string
        self.save()
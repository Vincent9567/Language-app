from django.test import TestCase
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class Test_User_Profile(TestCase):

    def test_001_profile_is_created(self):
            
            test_user_1 = UserProfile(
                user_name = 'Vincent9567', 
                user_email = 'vrusso9567@gmail.com', 
                target_language = 'Spanish', 
                native_language = 'English', 
                words_learned = 0, 
                active_cards = 0
            )

            test_user_1.full_clean()
            self.assertIsNotNone(test_user_1)
        
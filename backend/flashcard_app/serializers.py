from rest_framework import serializers
from .models import FlashCard
from target_language_app.models import TargetLanguage
from user_profile_app.models import UserProfile
from target_language_app.serializers import TargetLanguageSerializer
from user_profile_app.serializers import UserProfileSerializer

class FlashCardSerializer(serializers.ModelSerializer):
    language_id = TargetLanguageSerializer(many=False)
    user_id = UserProfileSerializer(many=False)

    class Meta:
        model = FlashCard
        fields = ('id','user_id', 'language_id', 'foreign_word', 'native_translation', 'times_seen', 'difficulty_rating')

    def create(self, validated_data):
        language_data = validated_data.pop('language_id')
        user_data = validated_data.pop('user_id')

        # Get or create TargetLanguage
        language, _ = TargetLanguage.objects.get_or_create(
            language_name=language_data['language_name']
        )

        # Retrieve the existing UserProfile or create a new one if it doesn't exist
        user = UserProfile.objects.filter(user_name=user_data['user_name']).first()
        if not user:
            user = UserProfile.objects.create(
                user_name=user_data['user_name'],
                user_email=user_data['user_email'],
                target_language_id=language,
                target_language=user_data['target_language'],
                native_language=user_data['native_language'],
                active_cards=user_data['active_cards'],
                words_learned=user_data['words_learned'],
            )

        flashcard = FlashCard.objects.create(language_id=language, user_id=user, **validated_data)
        return flashcard

    def update(self, instance, validated_data):
        language_data = validated_data.pop('language_id', None)
        user_data = validated_data.pop('user_id', None)

        if language_data:
            language, _ = TargetLanguage.objects.get_or_create(
                language_name=language_data['language_name']
            )
            instance.language_id = language

        if user_data:
            # Retrieve the existing UserProfile or create a new one if it doesn't exist
            user = UserProfile.objects.filter(user_name=user_data['user_name']).first()
            if not user:
                user = UserProfile.objects.create(
                    user_name=user_data['user_name'],
                    user_email=user_data['user_email'],
                    target_language_id=instance.language_id,
                    target_language=user_data['target_language'],
                    native_language=user_data['native_language'],
                    active_cards=user_data['active_cards'],
                    words_learned=user_data['words_learned'],
                )
            instance.user_id = user

        instance.foreign_word = validated_data.get('foreign_word', instance.foreign_word)
        instance.native_translation = validated_data.get('native_translation', instance.native_translation)
        instance.times_seen = validated_data.get('times_seen', instance.times_seen)
        instance.difficulty_rating = validated_data.get('difficulty_rating', instance.difficulty_rating)
        instance.save()
        return instance
    

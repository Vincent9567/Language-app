from rest_framework import serializers
from .models import UserProfile
from target_language_app.models import TargetLanguage
from target_language_app.serializers import TargetLanguageSerializer

class UserProfileSerializer(serializers.ModelSerializer):

    target_language_id = TargetLanguageSerializer(many=False)

    class Meta:
        model = UserProfile
        fields = ('id','user_name','password', 'user_email', 'target_language_id', 'target_language', 'native_language', 'active_cards', 'words_learned')
        
    def to_internal_value(self, data):
        if isinstance(data, dict):
            user = UserProfile.objects.filter(user_name=data.get('user_name')).first()
            if user:
                return {
                    'id': user.id,
                    'user_name': user.user_name,
                    'password': user.password,
                    'user_email': user.user_email,
                    'target_language_id': user.target_language_id.id,
                    'target_language': user.target_language,
                    'native_language': user.native_language,
                    'active_cards': user.active_cards,
                    'words_learned': user.words_learned,
                }
        return super().to_internal_value(data)


    def create(self, validated_data):
        # Extract and remove nested data for target_language_id
        language_data = validated_data.pop('target_language_id')
        
        # Check if the target language already exists
        language, _ = TargetLanguage.objects.get_or_create(
            language_name=language_data['language_name']
        )
        
        if not language:
            language = TargetLanguage.objects.create(**language_data)
        
        # Create the new user profile with the retrieved language
        new_user = UserProfile.objects.create(target_language_id=language, **validated_data)
        return new_user
    
    
    def update(self, instance, validated_data):
        language_data = validated_data.pop('language_id', None)

        if language_data:
            language, _ = TargetLanguage.objects.get_or_create(
                language_name=language_data['language_name']
            )
            instance.language_id = language

        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.target_language = validated_data.get('target_language', instance.target_language)
        instance.native_language = validated_data.get('native_language', instance.native_language)
        instance.active_cards = validated_data.get('active_cards', instance.active_cards)
        instance.words_learned = validated_data.get('words_learned', instance.words_learned)
        instance.save()
        return instance
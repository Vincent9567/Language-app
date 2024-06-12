from rest_framework import serializers
from .models import TargetLanguage

class TargetLanguageSerializer(serializers.ModelSerializer):

    class Meta:

        model = TargetLanguage
        fields = ('id', 'language_name')

    def to_internal_value(self, data):
        if isinstance(data, dict):
            language = TargetLanguage.objects.filter(language_name=data.get('language_name')).first()
            if language:
                return {
                    'id': language.id,
                    'language_name': language.language_name,
                }
        return super().to_internal_value(data)
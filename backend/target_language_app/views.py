from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import TargetLanguage
from django.core.serializers import serialize
from .serializers import TargetLanguageSerializer
import json

# Create your views here.

class AllTargetLanguages(APIView):

    def get(self, request):

        languages = TargetLanguage.objects.order_by('language_name')
        languages_serialized = TargetLanguageSerializer(languages, many=True)

        return Response(languages_serialized.data)
    
    def post(self, request):

        new_language = TargetLanguage.objects.create(**request.data)
        new_language.save()
        new_language.full_clean()
        new_language_serialized = TargetLanguageSerializer(new_language, many=False)
        return Response(new_language_serialized.data)
    

class SelectedTargetLanguage(APIView):

    def get_language(self, id):
    
        if type(id) == int:
            return TargetLanguage.objects.get(id = id)
        else:
            return TargetLanguage.objects.get(language_name = id)
        

    def get(self, request, id):

        selected_language = self.get_language(id)
        selected_language_serialized = TargetLanguageSerializer(selected_language, many=False)
        return Response(selected_language_serialized.data)
    
    def put(self, request, id):

        selected_language = self.get_language(id)

        if 'language_name' in request.data:
            selected_language.language_name = request.data['language_name']
        
        selected_language.save()
        selected_language.full_clean()

        selected_language_serialized = TargetLanguageSerializer(selected_language, many=False)
        return Response(selected_language_serialized.data)
    
    def delete(self, request, id):

        selected_language = self.get_language(id)
        selected_language_name = selected_language.language_name
        selected_language.delete()

        return Response(f'{selected_language_name} has been deleted!')
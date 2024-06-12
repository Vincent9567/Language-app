from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import FlashCard
from django.core.serializers import serialize
from .serializers import FlashCardSerializer
import json

# Create your views here.

class AllFlashCards(APIView):

    def get(self, request):

        flashcards = FlashCard.objects.order_by('foreign_word')
        flashcards_serialized = FlashCardSerializer(flashcards, many=True)

        return Response(flashcards_serialized.data)
    
    def post(self, request):

        serializer = FlashCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SelectedFlashCard(APIView):

    def get_flashcard(self, id):
    
        if type(id) == int:
            return FlashCard.objects.get(id=id)
        else:
            return FlashCard.objects.get(native_translation = id)
        
    def get(self, request, id):

        selected_user = self.get_flashcard(id)
        selected_user_serialized = FlashCardSerializer(selected_user, many=False)
        return Response(selected_user_serialized.data)
    
    def put(self, request, id):

        selected_user = self.get_flashcard(id)
        selected_language_serialized = FlashCardSerializer(selected_user, data=request.data)
        
        if selected_language_serialized.is_valid():
            selected_language_serialized.save()
            return Response(selected_language_serialized.data, status=status.HTTP_201_CREATED)
        return Response(selected_language_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):

        selected_card = self.get_flashcard(id)
        selected_foreign_word = selected_card.foreign_word
        selected_card.delete()

        return Response(f'{selected_foreign_word} has been deleted!')
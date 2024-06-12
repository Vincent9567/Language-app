from django.urls import path, register_converter
from .views import AllFlashCards, SelectedFlashCard
from .converters import IntOrStrConverter
# Remember all urls are prefaced by http://localhost:8000/api/v1/flashcards/

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    # Currently only takes GET requests
    path('', AllFlashCards.as_view(), name='all_flashcards'),
    path('<int_or_str:id>/', SelectedFlashCard.as_view(), name='selected_flashcard'),
]




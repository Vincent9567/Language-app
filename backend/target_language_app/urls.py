from django.urls import path, register_converter
from .views import AllTargetLanguages, SelectedTargetLanguage
from .converters import IntOrStrConverter

# Remember all urls are prefaced by http://localhost:8000/api/v1/languages/

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', AllTargetLanguages.as_view(), name='all_languages'),
    path('<int_or_str:id>/', SelectedTargetLanguage.as_view(), name='selected_language'),
]
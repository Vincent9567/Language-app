from django.urls import path, register_converter
from .views import AllUserProfiles, SelectedUserProfile
from .converters import IntOrStrConverter
# Remember all urls are prefaced by http://localhost:8000/api/v1/userprofiles/

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', AllUserProfiles.as_view(), name='all_user_profiles'),
    path('<int_or_str:id>/', SelectedUserProfile.as_view(), name='selected_user_profile'),
]
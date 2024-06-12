from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import UserProfile
from target_language_app.models import TargetLanguage
from django.core.serializers import serialize
from .serializers import UserProfileSerializer
import json


class AllUserProfiles(APIView):

    def get(self, request):

        user_profiles = UserProfile.objects.order_by('user_name')
        user_profiles_serialized = UserProfileSerializer(user_profiles, many=True)

        return Response(user_profiles_serialized.data)
    
    def post(self, request):

        print('here is the request', request.data)
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SelectedUserProfile(APIView):

    def get_user_profile(self, id):
    
        if type(id) == int:
            return UserProfile.objects.get(id=id)
        else:
            return UserProfile.objects.get(user_name = id)
        
    def get(self, request, id):

        selected_user = self.get_user_profile(id)
        selected_user_serialized = UserProfileSerializer(selected_user, many=False)
        return Response(selected_user_serialized.data)
    
    def put(self, request, id):

        selected_user = self.get_user_profile(id)
        selected_language_serialized = UserProfileSerializer(selected_user, data=request.data)
        
        if selected_language_serialized.is_valid():
            selected_language_serialized.save()
            return Response(selected_language_serialized.data, status=status.HTTP_201_CREATED)
        return Response(selected_language_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):

        selected_user = self.get_user_profile(id)
        selected_user_name = selected_user.user_name
        selected_user.delete()

        return Response(f'{selected_user_name} has been deleted!')
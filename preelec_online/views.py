from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class UserDetail(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            user = request.user
            serializer = UserSerializer(user, read_only = True)
            return Response(serializer.data)
        else: return Response(status=status.HTTP_404_NOT_FOUND)
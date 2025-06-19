from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserMeView(APIView):
    def get(self, request):
        data = {
            "username": "testuser",
            "email": "testuser@example.com"
        }
        return Response(data, status=status.HTTP_200_OK)

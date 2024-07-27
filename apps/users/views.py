
from rest_framework import generics
from rest_framework.response import Response

from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import UserSerializer, UserSignUpSerializer, UserSignInSerializer 
from .models import User


class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer
    
class UserProfile(CustomLoginRequiredMixin,generics.RetrieveAPIView):
    serializer_class = UserSerializer
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user],many =True)
        return Response(serializer.data[0])

    


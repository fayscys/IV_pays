from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserSignInSerializer

# Create your views here.

@permission_classes([AllowAny])
class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer

@permission_classes([AllowAny])
class UserSignInView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSignInSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        token_data = {}
        token_data['refresh'] = str(refresh)
        token_data['access'] = str(refresh.access_token)
        return Response(token_data, status=status.HTTP_200_OK)

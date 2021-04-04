from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView

from .serializers import CreateUserSerializers
from ..models import Account


class UserRegistration(CreateAPIView):
    serializer_class = CreateUserSerializers
    queryset = Account.objects.all()


class UserLogin(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

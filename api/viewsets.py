from rest_framework import viewsets
from users.models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import action


class profileviewset(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = profileSerializer


class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


class roleviewset(viewsets.ModelViewSet):
    queryset = role.objects.all()
    serializer_class = roleserializer


class permissionviewset(viewsets.ModelViewSet):
    queryset = permission.objects.all()
    serializer_class = permissionerializer

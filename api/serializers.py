from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from users.models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'first_name', 'last_name', 'email']
        # fields = "__all__"


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = "__all__"


class permissionerializer(serializers.ModelSerializer):
    class Meta:
        model = permission
        fields = "__all__"


class roleserializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = "__all__"

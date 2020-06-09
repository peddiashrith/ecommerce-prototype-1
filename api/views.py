from django.shortcuts import render, HttpResponse, get_object_or_404
from users.models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class userList(APIView):
    def get(self, request):
        allusers = User.objects.all()
        myserializer = userSerializer(allusers, many=True)
        return Response(myserializer.data)

    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mydata = serializer.data
            myuser = User.objects.get(username=mydata['username'])
            profile.objects.create(user=myuser)
            print("Serializers: ", serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(User, id=id)

    def get(self, request, id):
        myuser = self.get_object(id)
        serializer = userSerializer(myuser)
        return Response(serializer.data)

    def put(self, request, id):
        employee = self.get_object(id)
        serializer = userSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

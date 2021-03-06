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


class userlogin(APIView):
    def get(self, request):
        allusers = User.objects.all()
        myserializer = userSerializer(allusers, many=True)
        return Response(myserializer.data)

    def post(self, request):
        serializer = userSerializer(data=request.data)
        mydata = serializer.initial_data
        print(mydata)
        username = mydata["username"]
        fetch_user = User.objects.filter(username=username)
        if len(fetch_user) == 0:
            return Response({'login': 'invalid'}, status.HTTP_403_FORBIDDEN)
        else:
            myuser = fetch_user[0]
            if myuser.username == mydata["username"] and myuser.password == mydata["password"]:
                return Response({'login': 'success'}, status.HTTP_202_ACCEPTED)
            else:
                return Response({'login': 'invalid'}, status.HTTP_403_FORBIDDEN)


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

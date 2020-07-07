from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView

# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from loginapi.models import Task
from loginapi.serializers import UserSerializer, UserCreateSerializer, taskViewSerializer


class userView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class taskView(ListAPIView):
    serializer_class = taskViewSerializer
    queryset = Task.objects.all()

class taskCreate(CreateAPIView):
    serializer_class = taskViewSerializer
    queryset = Task.objects.all()

class taskDetail(RetrieveAPIView):
    serializer_class = taskViewSerializer
    queryset = Task.objects.all()


class taskEdit(RetrieveUpdateAPIView):
    serializer_class = taskViewSerializer
    queryset = Task.objects.all()

class taskDelete(RetrieveDestroyAPIView):
    serializer_class = taskViewSerializer
    queryset = Task.objects.all()
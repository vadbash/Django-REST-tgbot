from django.shortcuts import render
from .models import ChatbotUsers, MessageHistory
from rest_framework import viewsets
from .serializers import UserSerializer, MessageHistorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = ChatbotUsers.objects.all().order_by('-reg_date')
    serializer_class = UserSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer

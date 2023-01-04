from .models import ChatbotUsers, MessageHistory
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatbotUsers
        fields = ('chat_id', 'full_name', 'username', 'language_code', 'reg_date')


class MessageHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ('message_id', 'chat_id', 'full_name', 'username', 'date', 'text')
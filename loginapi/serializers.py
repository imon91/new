from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from loginapi.models import Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email'

        ]
        extra_kwargs = {"password":
                            {"write_only": True}}


class UserCreateSerializer(ModelSerializer):
    # email2 = serializers.EmailField(label='confirm mail')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email'

        ]
        extra_kwargs = {"password":
                            {"write_only": True}}

    # def validate(self, data):
    #     email = data['email']
    #     user_qs = User.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise ValidationError("This user has already  ")
    # #
    # def validate_email2(self, value):
    #     data = self.get_initial()
    #     print(value)
    #
    #     email1 = data.get("email")
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError("email must be matched")

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        Token.objects.create(user=user_obj)
        return validated_data

class taskViewSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'completed'

        ]
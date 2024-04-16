
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from .models import User
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=123, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(max_length=123, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar',
                  'password1', 'password2', 'created_date']

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        user = super().create(validated_data)
        user.set_password(password1)
        user.save()
        return user


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar',
                  'last_login', 'modified_date', 'created_date']
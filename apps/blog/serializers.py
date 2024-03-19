from rest_framework import serializers
from apps.account.models import User
from .models import (
    Subblog,
    Blog,
    Tags,
    Categories,
    Comments,
    Services,
    Profession,
    Results,
    Skills
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name',]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class ServicesSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'author', 'name', 'content']

    def create(self, validated_data):
        user_id = self.context['user_id']
        validated_data['author_id'] = user_id
        return super().create(validated_data)

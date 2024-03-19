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
        fields = ['id', 'username']


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


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

    def create(self, validated_data):
        user_id = self.context['user_id']
        validated_data['author_id'] = user_id
        return super().create(validated_data)


class ResultsSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='get_unit_display', read_only=True)

    class Meta:
        model = Results
        fields = ['id', 'unit_name', 'unit', 'name', 'company', 'content', 'created_time', 'deleted_time',]


class SkillsSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='get_unit_display', read_only=True)

    class Meta:
        model = Skills
        fields = ['id', 'name', 'unit_name', 'unit', 'full', 'Last_week', 'Last_month']


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    category_unit = serializers.CharField(source='get_category_unit_display', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'slug', 'name', 'author', 'tags',
                  'category', 'category_unit', 'image', 'footer_content',
                  'header_content', 'author_message']

    def create(self, validated_data):
        user_id = self.context['user_id']
        validated_data['author_id'] = user_id
        return super().create(validated_data)


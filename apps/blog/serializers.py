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


class ServicesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'content']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['author_id'] = request.user.id
        return super().create(validated_data)


class ProfessionsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Profession
        fields = ['author', 'name']


class ProfessionsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['name']

    def create(self, validated_data):
        user_id = self.context['request'].user.id
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


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['name', 'tags',
                  'category', 'image', 'footer_content',
                  'header_content', 'author_message']

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        validated_data['author_id'] = user_id
        return super().create(validated_data)


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'name', 'tags',
                  'category', 'image', 'footer_content',
                  'header_content', 'author_message', 'slug', 'created_date']

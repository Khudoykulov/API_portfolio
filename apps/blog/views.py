from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    TagsSerializer,
    CategoriesSerializer,
    ServicesSerializer,
    ProfessionsSerializer,
    ResultsSerializer,
    SkillsSerializer,
    BlogSerializer

)
from .models import (
    Tags,
    Categories,
    Services,
    Profession,
    Results,
    Skills, Blog
)


class TagViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated]


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated]


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthorOrReadOnly]


class ProfessionsViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionsSerializer
    permission_classes = [IsAuthorOrReadOnly]


class ResultsViewSet(ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthorOrReadOnly]


class SkillsViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthorOrReadOnly]


class BlogsListCreateViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogSerializer
        return BlogSerializer


class BlogsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'slug'


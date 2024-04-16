from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
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
    ProfessionsPostSerializer,
    ResultsSerializer,
    SkillsSerializer,
    BlogPostSerializer,
    BlogSerializer,
    ServicesPostSerializer

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
    serializer_post_class = ServicesPostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ServicesSerializer
        return ServicesPostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'delete'})


class ProfessionsViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionsSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProfessionsSerializer
        return ProfessionsPostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'delete'})


class ResultsViewSet(ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthorOrReadOnly]


class SkillsViewSet(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthorOrReadOnly]


class BlogsListCreateViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogSerializer
        return BlogPostSerializer


class BlogsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'slug'


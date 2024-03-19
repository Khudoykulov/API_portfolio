from django.urls import path, include
from .views import (
    TagViewSet,
    CategoriesViewSet,
    ServicesViewSet,
    ProfessionsViewSet,
    ResultsViewSet,
    SkillsViewSet,
    BlogsListCreateViews,
    BlogsRUDAPIView

)
from rest_framework.routers import DefaultRouter

routerTag = DefaultRouter()
routerTag.register('tags', TagViewSet, basename='tags')

routerCategory = DefaultRouter()
routerCategory.register('category', CategoriesViewSet, basename='category')

routerService = DefaultRouter()
routerService.register('services', ServicesViewSet, basename='services')

routerProfessions = DefaultRouter()
routerProfessions.register('professions', ProfessionsViewSet, basename='professions')

routerResults = DefaultRouter()
routerResults.register('results', ResultsViewSet, basename='results')

routerSkills = DefaultRouter()
routerSkills.register('skill', SkillsViewSet, basename='skill')

app_name = 'blog'

urlpatterns = [
    path('', include(routerTag.urls)),
    path('', include(routerCategory.urls)),
    path('', include(routerService.urls)),
    path('', include(routerProfessions.urls)),
    path('', include(routerResults.urls)),
    path('', include(routerSkills.urls)),
    path('list-create/', BlogsListCreateViews.as_view(), name='list-create'),
    path('list-rud/<slug:slug>/', BlogsRUDAPIView.as_view(), name='list-rud'),
]


from django.urls import path, include
from .views import (
    TagViewSet,
    CategoriesViewSet,
    ServicesViewSet,

)
from rest_framework.routers import DefaultRouter

routerTag = DefaultRouter()
routerTag.register('tags', TagViewSet, basename='tags')

routerCategory = DefaultRouter()
routerCategory.register('category', CategoriesViewSet, basename='category')

routerService = DefaultRouter()
routerService.register('services', ServicesViewSet, basename='services')

app_name = 'blog'

urlpatterns = [
    path('', include(routerTag.urls)),
    path('', include(routerCategory.urls)),
    path('', include(routerService.urls)),
]


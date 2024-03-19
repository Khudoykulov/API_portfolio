from django.contrib import admin
from .models import (
    Partners,
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


class PartnersInline(admin.TabularInline):
    model = Partners
    extra = 0


class CommentsInline(admin.TabularInline):
    fields = ('id', 'name')
    model = Comments
    extra = 0


class SubblogAdminInline(admin.TabularInline):
    model = Subblog
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category', 'created_date',)
    list_display_links = ('id', 'name', 'category', 'created_date',)
    search_fields = ('name',)
    readonly_fields = ('created_date', 'slug')
    date_hierarchy = 'created_date'
    # autocomplete_fields = ('author',)
    filter_horizontal = ('tags',)
    inlines = [SubblogAdminInline,  CommentsInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'content', 'created_date',)
    list_display_links = ('id', 'name', 'content', 'created_date',)
    search_fields =('name',)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name')
    list_display_links = ('id', 'author', 'name')
    search_fields = ('name',)


@admin.register(Results)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'created_date',)
    list_display_links = ('id', 'name', 'content', 'created_date',)
    search_fields = ('name', 'unit')
    readonly_fields = ('created_date',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit',)
    list_display_links = ('id', 'name', 'unit',)
    search_fields = ('name', 'unit')

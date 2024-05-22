import django_filters

from .models import Blog, Tags


class EpisodeFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(lookup_name='category')
    tags = django_filters.CharFilter(method='filter_by_tags')

    def filter_by_tags(self, queryset, name, value):
        if value:
            tag_ids = [int(id) for id in value.split(',')]
            queryset = queryset.filter(tags__in=tag_ids)
        return queryset

    class Meta:
        model = Blog
        fields = ['tags', 'category']


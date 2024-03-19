from django.db import models
from apps.account.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save


class Tags(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    tags = models.ManyToManyField(Tags, related_name='tags')
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    header_content = RichTextField(null=True, blank=True)
    footer_content = RichTextField(null=True, blank=True)
    author_message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=123, unique=True)

    def __str__(self):
        return self.name


class Subblog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True, related_name='subblog')
    name = models.CharField(max_length=123)
    content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=123)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def children(self):
        if not self.top_level_comment_id:
            return Comments.objects.filter(top_level_comment_id=self.id)
        return None

    def __str__(self):
        return self.name


class Services(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=123)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profession(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='profession')
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Results(models.Model):
    UNIT = (
        (0, 'Education'),
        (1, 'Experience'),
        (3, 'Awards')
    )
    unit = models.IntegerField(choices=UNIT,)
    name = models.CharField(max_length=123)
    company = models.CharField(max_length=123)
    created_time = models.DateField()
    deleted_time = models.DateField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    UNIT = (
        (0, 'Top'),
        (1, 'low')
    )
    unit = models.IntegerField(choices=UNIT, default=1)
    name = models.CharField(max_length=123)
    full = models.IntegerField()
    Last_week = models.IntegerField(null=True, blank=True)
    Last_month = models.IntegerField(null=True, blank=True)


def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().date().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=Blog)


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


pre_save.connect(comment_pre_save, sender=Comments)
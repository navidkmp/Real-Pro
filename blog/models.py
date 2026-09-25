from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ManyToManyField(Category, related_name='blog_posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )


    def get_absolute_url(self):
        return reverse(
            'blog:blog_detail',
            kwargs={'slug': self.slug}
        )


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created_at']

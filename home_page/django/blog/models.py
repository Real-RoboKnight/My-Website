from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    sort_order = models.PositiveIntegerField(default=0, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    related_posts = models.ForeignKey(
        "PostStream", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-sort_order", "-updated_at"]


class PostStream(models.Model):
    title = models.CharField(max_length=200)
    posts = models.ManyToManyField(BlogPost, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

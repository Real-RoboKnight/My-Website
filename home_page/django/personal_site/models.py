from django.db import models
from blog.models import PostStream


class HomepageStream(models.Model):
    class Column(models.TextChoices):
        WIDE = "wide", "Wide"
        NARROW = "narrow", "Narrow"

    stream = models.ForeignKey(PostStream, on_delete=models.CASCADE)
    column = models.CharField(max_length=10, choices=Column.choices)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self) -> str:
        return f"{self.stream} ({self.column})"

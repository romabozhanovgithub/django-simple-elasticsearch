from django.db import models
from django.contrib.auth.models import User

ARTICLE_TYPES = [
    ("UN", "Unspecified"),
    ("TU", "Tutorial"),
    ("RS", "Research"),
    ("RW", "Review"),
]

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article_type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default="UN")
    categories = models.ManyToManyField(to=Category, blank=True, related_name="categories")
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.title} ({self.created_datetime.date()})"

    def type_to_string(self):
        if self.article_type == "UN":
            return "Unspecified"
        elif self.article_type == "TU":
            return "Tutorial"
        elif self.article_type == "RS":
            return "Research"
        elif self.article_type == "RW":
            return "Review"

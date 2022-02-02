from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.get_users, name="users"),
    path("user/<int:pk>/", views.get_user, name="user"),
    path("category/", views.get_categories, name="categories"),
    path("category/<int:pk>/", views.get_category, name="category"),
    path("article/", views.get_articles, name="articles"),
    path("article/<int:pk>/", views.get_article, name="article"),
]

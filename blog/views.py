from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Category, Article
from blog.serializers import CategorySerializer, ArticleSerializer, UserSerializer

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_user(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serailizer.data)

@api_view(["GET"])
def get_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = UserSerializer(category, many=False)
    return Response(serailizer.data)

@api_view(["GET"])
def get_articles(request):
    articles = Article.objects.all()
    print(articles)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_article(request, pk):
    article = Article.objects.get(id=pk)
    serializer = UserSerializer(article, many=False)
    return Response(serializer.data)

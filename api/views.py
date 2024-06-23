from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from my_first_web.models import Category, Course
from .serializers import CourseSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import logging

logger = logging.getLogger(__name__)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.none()  # Изменено на пустой queryset
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        base_query = Course.objects.all()
        category_name = self.request.query_params.get('category', None)

        if category_name:
            try:
                category = Category.objects.get(title=category_name)
                filtered_query = base_query.filter(category=category)
                return filtered_query
            except Category.DoesNotExist:
                logger.error(f'Category with title "{category_name}" does not exist.')
                return base_query  # Возвращаем исходный queryset, если категория не найдена

        return base_query


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

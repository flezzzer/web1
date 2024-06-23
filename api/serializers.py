from my_first_web.models import Category, Course
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        queryset = model.objects.all()
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        queryset = model.objects.all()
        fields = '__all__'


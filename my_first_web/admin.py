from django.contrib import admin
from . import models

admin.site.site_header="Courses Admin"
admin.site.site_title="My courses"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','category','price')

class CoursesInline(admin.TabularInline):
    model=models.Course
    exclude = ['created_at']
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    fieldsets = [(None,{'fields': ['title']}),
                 ('Dates',
                  {'fields':['created_at'],
                   'classes': ['collapse']})]
    inlines = [CoursesInline]

admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Category, CategoryAdmin)
# Register your models here.

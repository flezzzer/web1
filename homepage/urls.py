from django.urls import path,include

import api.urls
from . import views


urlpatterns=[
    path('', views.index)
]

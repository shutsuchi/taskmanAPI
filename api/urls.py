from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api.views import TaskViewSet, CreateUserView, MyProfileView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('myself', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]
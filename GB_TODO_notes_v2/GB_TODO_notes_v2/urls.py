"""GB_TODO_notes_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from GB_TODO_notes_v2.views import UserCustomViewSet, ToDoListAPIView, ToDoDetailAPIView, ProjectDjangoFilterViewSet, \
    ToDoDjangoFilterViewSet
from todo.views import ProjectModelViewSet, TODOModelViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TODOModelViewSet)
# router.register('todos', ToDoDjangoFilterViewSet)
# router.register('projects', ProjectDjangoFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api-todo/', ToDoListAPIView.as_view()),
    path('api-todo/<int:pk>/', ToDoDetailAPIView.as_view()),
]

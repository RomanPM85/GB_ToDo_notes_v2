# GB_TODO_notes
## Практическое задание (проект) Geekbrains курса Django Rest Framework DRF

### Последовательность действий tasks lesson-1

1. Создать новый проект на github или gitlab.
2. Создать django-проект.
3. Установить DRF и подключить его к django-проекту.
4. Создать приложение для работы с пользователем.
5. Создать свою модель пользователя. 
6. В ней поле email сделать уникальным.
7. Сделать для неё базовое API — по аналогии модели Author. В качестве полей выбрать
username, firstname, lastname, email. Если выбрать все поля, при попытке сериализации может
возникнуть ошибка сериализации связанного поля. Эту тему мы рассмотрим далее.
8. Подключить стандартную админку.
9. Создать суперпользователя.
10. (Задание со *) Создать management command — скрипт для запуска через manage.py для автоматического создания
суперпользователя и нескольких тестовых пользователей(Management commands).
11. Сдать работу в виде ссылки на репозиторий с кодом.

#### Создание и настройка проекта:
pip install django==3.2.8  # Установка фреймворка.
django-admin startproject GB_TODO_notes  # Создание проекта

pip install djangorestframework  # Установка DRF
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

#### Создаем модель Users:
        class Users(models.Model):
            user_name = models.CharField(max_length=64)
            first_name = models.CharField(max_length=64)
            last_name = models.CharField(max_length=64)
            email = models.EmailField(max_length=70, unique=True)
        
            def __str__(self):
                return f'{self.last_name}-{self.first_name}'

#### Проводим миграции в БД
python3 manage.py makemigrations
python3 manage.py migrate

#### Создаем файл serializers.py и создаем класс сериализации.
        class UsersModelSerializer(ModelSerializer):
            class Meta:
                model = Users
                fields = '__all__'

#### Создаем класс в views.py

        from rest_framework.viewsets import ModelViewSet
        from .serializers import UsersModelSerializer
        from .models import Users


        class UsersModelViewSet(ModelViewSet):
            queryset = Users.objects.all()
            serializer_class = UsersModelSerializer

### Корректируем файл urls.py
        from rest_framework.routers import DefaultRouter
        from users.views import UsersModelViewSet
        
        router = DefaultRouter()
        router.register('users', UsersModelViewSet)
        
        urlpatterns = [
            path('api/', include(router.urls)),
        ]

### Создаем суперпользователя для админки
python manage.py createsuperuser

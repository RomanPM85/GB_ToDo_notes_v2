# GB_TODO_notes
## Практическое задание (проект) Geekbrains курса Django Rest Framework DRF

## Последовательность действий tasks lesson-1

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
#### Создание нужных пакетов
    pip freeze > requirements.txt

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

#### Корректируем файл urls.py
        from rest_framework.routers import DefaultRouter
        from users.views import UsersModelViewSet
        
        router = DefaultRouter()
        router.register('users', UsersModelViewSet)
        
        urlpatterns = [
            path('api/', include(router.urls)),
        ]

#### Создаем суперпользователя для админки
    python manage.py createsuperuser

## Последовательность действий tasks lesson-2

### Создание frontend через REST фреймворк

#### Создание приложение: 
    npx create-react-app frontend

#### Для запуска тестового сервера выполняем:
    npm run start

#### Главное приложение (/frontend/src/App.js):
    
    import React from 'react';
    import logo from './logo.svg';
    import './App.css';
    

    class App extends React.Component {
        constructor(props) {
            super(props)
            this.state = {
                'users': []
            };
        }
        render() {
            return(
                <div>Main App</div>
            )
        }
    }
    export default App;
    
#### Компонент для отображения одного автора (/frontend/src/components/User.js):
    import React from 'react'
    
    const UserItem = ({user}) => {
        return (
            <tr>
                <td>
                    {user.user_name}
                </td>
                <td>
                    {user.first_name}
                </td>
                <td>
                    {user.last_name}
                </td>
                <td>
                    {user.email}
                </td>
            </tr>
        )
    }
#### Компонент для списка авторов (/frontend/src/components/User.js):
    const UserList = ({users}) => {
    
        return (
            <table>
                <th>
                    User name
                </th>
                <th>
                    First name
                </th>
                <th>
                    Last name
                </th>
                <th>
                    Email user
                </th>
                {users.map((user) => <UserItem user={user} />)}
            </table>
        )
    }
    export default UserList;
#### Настройка политики CORS
    pip install django-cors-headers

#### Обновление нужных пакетов
    pip freeze > requirements.txt

#### Добавляем приложение в INSTALLED_APPS (/GB_TODO_notes_v2/settings.py)
    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]
#### Подключаем 'corsheaders.middleware.CorsMiddleware в MIDDLEWARE.(/library/settings.py)
    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]
#### И в settings.py проекта добавляем адреса, с которых будет возможен запрос.(/library/settings.py)
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000/",
    ]


#### Отправка запроса с front-end на back-end
#### Устанавливаем axios.
    npm install axios
#### Общий вид отправки запроса с помощью axios имеет следующий вид:

    axios.get(<url>)
        .then(response => {
            <действия с response>
        }).catch(error => <действия с error>)

#### Получение и обработка ответа с back-end
#### В файле App.js импортируем axios.
    import axios from 'axios'
#### Изменим метод ComponentDidMount в классе App следующим образом:
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => console.log(error))
    }

    export default App;

#### Добавить на страницу компоненты Menu и Footer (/frontend/src/components/Menu.js, Footer.js):
##### И внесем в файл следующий код (/frontend/src/components/Menu.js):
    import React from "react";

    const MenuItem = ({menu}) => {
        return (
                <ul>
                    <li> <a href="#">HOME</a></li>
                    <li> <a href="#">ListUsers</a></li>
                    <li> <a href="#">ListNotes</a></li>
                </ul>
        )
    }
    export default MenuItem;
##### И внесем в файл следующий код (/frontend/src/components/Footer.js):
    import React from "react";
    
    const FooterItem = ({footer}) => {
        return (
            <div class="footer">
                <div class="container">
                    <p>Copyrights © 2022 Footer GeekBrains ToDO Notes </p>
                </div>
            </div>
        )
    }
    
    export default FooterItem;

### В главное приложение внесем новые компоненты (/frontend/src/App.js):
    class App extends React.Component {
        ...
            <div>
                <MenuItem/>
                <UserList users={this.state.users}/>
                <FooterItem/>
            </div>
        ...
    }
    export default App;

## Последовательность действий tasks lesson-3
#### Задачи:
1. В проекте создать новое приложение для работы с TODO.
2. Добавить модель Project. Это проект, для которого записаны TODO. У него есть название,
может быть ссылка на репозиторий и набор пользователей, которые работают с этим
проектом. Создать модель, выбрать подходящие типы полей и связей с другими моделями.
3. Добавить модель TODO. Это заметка. У ToDo есть проект, в котором сделана заметка, текст
заметки, дата создания и обновления, пользователь, создавший заметку. Содержится и
признак — активно TODO или закрыто. Выбрать подходящие типы полей и связей с другими
моделями.
4. Создать API для моделей Projects и ToDo. Пока можно использовать ViewSets по аналогии с
моделью User.
5. При сериализации моделей выбрать нужный вид для связанных моделей.
6. (Задание со *) На стороне клиента используется camelCase в отличие от snake_case, который мы используем в python. Реализовать представление данных в виде camelCase(https://www.django-rest-framework.org/api-guide/parsers/#camelcase-json).

#### Созданием новое приложения для работы с TODO:
    python manage.py startapp todo

#### Регистрируем приложение в INSTALLED_APPS (/GB_TODO_notes_v2/settings.py):
    INSTALLED_APPS = [
        ...
        'todo',
        ...
    ]

#### Создаем модель Project и TODO:

    class Project(models.Model):
        title = models.CharField(max_length=24, blank=True, help_text='Заголовок проекта')
        linkGitHub = models.URLField(max_length=200, null=True, blank=True, help_text='Ссылка на репозиторий GitHub')
        users = models.ManyToManyField(User)
    
    
    class TODO(models.Model):
        STATUS_CHOICES = [
            ('ac', 'active'),
            ('сl', 'closed'),
        ]
        project = models.OneToOneField(Project, on_delete=models.CASCADE)
        text = models.TextField(null=True, blank=True, help_text='поле для заметок')
        create_publish = models.DateField(auto_now_add=True, help_text='поле даты создания заметки')
        update_publish = models.DateField(auto_now=True, help_text='поле даты обновления заметки')
        author = models.ForeignKey(User, blank=True, null=True, help_text='поля авто заметки')
        status = models.CharField(max_length=1, choices=STATUS_CHOICES, help_text='поле статуса,активная или закрыта')


#### Создаем сериализацию моделей Project и TODO (/GB_TODO_notes_v2/todo/serializers.py):
    touch serializers.py
##### Добавляем следующий код в (/GB_TODO_notes_v2/todo/serializers.py):
    from rest_framework.serializers import ModelSerializer
    from .models import Project, TODO
    
    
    class ProjectModelSerializer(ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'
    
    
    class TODOModelSerializer(ModelSerializer):
        class Meta:
            model = TODO
            fields = '__all__'

##### Создаем маршрутизаторы для приложения моделей Project ToDo (/GB_TODO_notes_v2/urls.py):
### Импортируем ViewSets
    from todo.views import ProjectModelViewSet, TODOModelViewSet

### Регистрируем
    router.register('todo', ProjectModelViewSet)
    router.register('todo', TODOModelViewSet)

#### Проводим миграции в БД
Проведем тестовый запуск миграций

    python manage.py makemigrations --dry-run

Если все хорошо, проводим миграции в БД

    python3 manage.py makemigrations
    python3 manage.py migrate

## Последовательность действий tasks lesson-4

1. Установить размер страницы для всех api 100 записей.
2. Выбрать подходящий класс для постраничного вывода.
3. В проекте доработать API следующим образом:
●
модель User: есть возможность просмотра списка и каждого пользователя в
отдельности, можно вносить изменения, нельзя удалять и создавать;
●
модель Project: доступны все варианты запросов; для постраничного вывода
установить размер страницы 10 записей; добавить фильтрацию по совпадению части
названия проекта;
●
модель ToDo: доступны все варианты запросов; при удалении не удалять ToDo, а
выставлять признак, что оно закрыто; добавить фильтрацию по проекту; для
постраничного вывода установить размер страницы 20.

## Создаем свои Views. 
### Доработка API модели User: (/GB_TODO_notes_v2/views.py)

#### Создаем класс UserCustomViewSet (/GB_TODO_notes_v2/views.py)
● модель User: есть возможность просмотра списка и каждого пользователя в отдельности, можно вносить изменения,
нельзя удалять и создавать; 

    class UserCustomViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
        """
        Custom ViewSet для модели User добавляем возможность просмотра списка и каждого пользователя в 
        отдельности, и возможность вносить изменения.
        """
        queryset = User.objects.all()
        serializer_class = UserModelSerializer
        renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

#### Создаем класс ProjectModelViewSet (/GB_TODO_notes_v2/todo/views.py)
● модель Project: доступны все варианты запросов;

    class ProjectModelViewSet(ModelViewSet):
        queryset = Project.objects.all()
        serializer_class = ProjectModelSerializer


#### Создаем класс ToDoListAPIView (/GB_TODO_notes_v2/views.py)
● класс для модели ToDo: доступны все варианты запросов; при удалении не удалять 
ToDo, а выставлять признак, что оно закрыто;

    class ToDoListAPIView(APIView):
        """
        Список всех созданных заметок к проекту и возможность
        создать новую заметку через метод POST.
        """
        renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
        def get(self, request, format=None):
            todo = TODO.objects.all()
            serializer = TODOModelSerializer(todo, many=True)
            return Response(serializer.data)
    
        def post(self, request, format=None):
            serializer = TODOModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

● Дополнительный класс для модели ToDo: 
при удалении не удалять ToDo, а выставлять признак, что оно закрыто;

    class ToDoDetailAPIView(APIView):
        """
        Класс для отображения одной записи с возможностью
        обновить частично обновить запись, а также при
        удалении перевести запись в закрытую.
        """
        def get_object(self, pk):
            try:
                return TODO.objects.get(pk=pk)
            except TODO.DoesNotExist:
                raise Http404
    
        def get(self, request, pk, format=None):
            todo = self.get_object(pk)
            serializer = TODOModelSerializer(todo)
            return Response(serializer.data)
    
        def put(self, request, pk, format=None):
            todo = self.get_object(pk)
            serializer = TODOModelSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        def delete(self, request, pk, format=None):
            todo = self.get_object(pk)
            serializer = TODOModelSerializer(todo, data={'status': 'с'}, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)


#### Создаем фильтрацию и пагинацию для моделей Project и TODO:
### Создадим файл filters.py (/GB_TODO_notes_v2/filters.py) для фильтрации и внесем следующий код: 

    from django_filters import rest_framework as filters
    from .models import Project, TODO
    
    
    class ProjectFilter(filters.FilterSet):
        title = filters.CharFilter(lookup_expr='contains')
    
        class Meta:
            model = Project
            fields = ['title']
    
    
    class ToDoFilter(filters.FilterSet):
        text = filters.CharFilter(lookup_expr='contains')
    
        class Meta:
            model = TODO
            fields = ['text', 'status']


### Внесем изменения в контроллеры, добавим дополнительные классы (/GB_TODO_notes_v2/views.py):

● для модель ToDo:

    class ToDoLimitOffsetPagination(LimitOffsetPagination):
        """
        Класс для модели ToDo ограниченного постраничного вывода информации. 
        """
        default_limit = 20
    

    class ToDoDjangoFilterViewSet(ModelViewSet):
        """
        Класс для фильтрации модели ToDo.
        """
        queryset = TODO.objects.all()
        serializer_class = TODOModelSerializer
        # filter_backends = [DjangoFilterBackend]
        filterset_class = ToDoFilter
        pagination_class = ToDoLimitOffsetPagination



● для модель Project: 

    class ProjectDLimitOffsetPagination(LimitOffsetPagination):
        """
        Класс для модели Project ограниченного постраничного вывода информации. 
        """
        default_limit = 10
    
    
    class ProjectDjangoFilterViewSet(ModelViewSet):
        """
        Класс для фильтрации модели Project.
        """
        queryset = Project.objects.all()
        serializer_class = ProjectModelSerializer
        filterset_class = ProjectFilter
        pagination_class = ProjectDLimitOffsetPagination



#### Добавим общие настройки фильтрации и пагинации для проекта Rest Framework.

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ],
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100
    }



## Последовательность действий tasks lesson-5
#### Устанавливаем библиотеку react-router-dom (/GB_TODO_notes_v2/frontend)
    npm install react-router-dom

#### Запускаем проект на frontend

    npm run start

## Последовательность действий tasks lesson-6
#### Устанавливаем общие права для всего проекта и укажем их в settings.py:

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],

        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ],
    }
## Последовательность действий tasks lesson-7
1. Создать компонент для авторизации с формой логина и пароля пользователя.
2. При отправке формы получить токен пользователя.
3. Сохранить токен пользователя в localStorage или cookies.
4. Добавить кнопку logout («выйти»). По нажатию на неё очищать токен в localStorage или
cookies.
5. Прикладывать токен к последующим запросам.
6. * На всех страницах отображать имя авторизованного пользователя и кнопку «Выйти», либо
кнопку «Войти», если пользователь не авторизован.

## Последовательность действий tasks lesson-8
1. Написать минимум один тест для API, используя APIRequestFactory.
2. Написать минимум один тест для API, используя APIClient.
3. Написать минимум один тест для API, используя APITestCase.
4. Данные для тестов удобно создавать, используя mixer.
5. * Написать минимум один Live test.

### Как запускать тесты

    python3 manage.py test

### Ещё больше тестовой информации
    python3 manage.py test --verbosity 2

### Запуск определённых тестов

    python manage.py test users.tests.TestUserViewSet.test_get_list
    python manage.py test users.tests.TestUserViewSet.test_create_guest
    python manage.py test users.tests.TestUserViewSet.test_create_admin

    python manage.py test users.tests.TestUserViewSet.test_get_detail
    python manage.py test users.tests.TestUserViewSet.test_edit_guest
    python manage.py test users.tests.TestUserViewSet.test_edit_admin

    python manage.py test users.tests.TestMath.test_sqrt
    python manage.py test users.tests.TestProjectsViewSet.test_get_list
    python manage.py test users.tests.TestProjectsViewSet.test_edit_admin
    python manage.py test users.tests.TestProjectsViewSet.test_edit_mixer


### Для быстрой генерации тестовых данных служит библиотека Mixer. Она позволяет создавать объекты и заполнять их тестовыми данными, а также создавать связанные объекты моделей.
    pip install mixer

### Запуск определённых тестов
    python manage.py test users.tests.TestProjectsViewSet.test_edit_mixer
    python manage.py test users.tests.TestProjectsViewSet.test_get_detail
    python manage.py test users.tests.TestProjectsViewSet.test_get_detail_users

## Последовательность действий tasks lesson-9

1) Создать новую версию API в проекте, в которой у модели пользователя будут доступны поля
is_superuser, is_staff. Таким образом, проект будет поддерживать две версии API.
2) Создать документацию для API, используя drf-yasg.
3) * Создать часть документации Swagger и/или ReDoc без использования сторонних библиотек.
Можно использовать минимальные примеры из стандартной документации Swagger и ReDoc.

###  Создаем новое приложение userapp:

    python manage.py startapp userapp

### В нём создадим файл serializers.py со следующим кодом:
/GB_TODO_notes_v2/userapp/serializers.py

    from django.contrib.auth.models import User
    from rest_framework import serializers

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email')

    class UserSerializerWithFullName(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email', 'first_name', 'last_name')

###  Далее в файле views.py напишем следующий код:
/GB_TODO_notes_v2/userapp/views.py

    from rest_framework import generics
    from django.contrib.auth.models import User
    from .serializers import UserSerializer, UserSerializerWithFullName
    
    
    class UserListAPIView(generics.ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
    
        def get_serializer_class(self):
            if self.request.version == '0.2':
                return UserSerializerWithFullName
            return UserSerializer

Если версия API 0.2, то мы будем использовать UserSerializerWithFullName, во всех остальных
случаях — UserSerializer.

###  Вариант использовать класс UrlPathVersioning: 
/GB_TODO_notes_v2/settings.py

    REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    ...
    }

### При использовании UrlPathVersioning мы можем передать номер версии в URL-адресе. В urls.py добавим следующий код:
/GB_TODO_notes_v2/urls.py

    urlpatterns = [
        ...
        re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
        ...
    ]


###  Вариант использования класса NamespaceVersioning
/GB_TODO_notes_v2/urls.py

    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    ...
    }
### В приложении userapp локально создадим файл urls.py со следующим кодом:
/GB_TODO_notes_v2/userapp/urls.py

    from django.urls import path
    from .views import UserListAPIView
    
    app_name = 'userapp'
    urlpatterns = [
        path('', UserListAPIView.as_view()),
    ]

Далее в urls.py всего проекта добавим следующий код:
/GB_TODO_notes_v2/urls.py

    urlpatterns = [
        ...
        path('api/users/0.1', include('userapp.urls', namespace='0.1')),
        path('api/users/0.2', include('userapp.urls', namespace='0.2')),
    ]

## Последовательность действий tasks lesson-10

1) С помощью GraphQL создать схему, которая позволит одновременно получать ToDo, проекты
и пользователей, связанных с проектом.
2) * Подумать, какие ещё гибкие запросы могут быть полезны для этой системы, реализовать
некоторые из них с помощью GraphQL.

### Установим библиотеку Graphene-Django:

    pip install graphene-django

### Добавим приложение в INSTALLED_APPS:
    INSTALLED_APPS = [
        ...
        "django.contrib.staticfiles", # Required for GraphiQL
        "graphene_django"
        ]

### В urls.py проекта добавим адрес для GraphQL-запросов:
    from django.urls import path
        from graphene_django.views import GraphQLView
        urlpatterns = [
        # ...
        path("graphql/", GraphQLView.as_view(graphiql=True)),
        ]
### Далее в settings.py указываем путь до объекта с описанием схемы:
    GRAPHENE = {
        "SCHEMA": "library.schema.schema"
        }

### Создадим файл schema.py и напишем в нём следующий код:
    from graphene import ObjectType
    from graphene_django import DjangoObjectType
    from users.models import User
    from todo.models import Project, TODO
    import graphene

#### Создадим класс для получения полей пользователей

    class UserType(DjangoObjectType):
        class Meta:
            model = User
            fields = '__all__'

#### Создадим класс для получения полей проектов

    class ProjectType(DjangoObjectType):
        class Meta:
            model = Project
            fields = '__all__'

#### Создадим класс для получения полей заметок

    class TODOType(DjangoObjectType):
        class Meta:
            model = TODO
            fields = '__all__'

#### Создадим класс серилизации

    class Query(ObjectType):
        all_users = graphene.List(UserType)
        all_project = graphene.List(ProjectType)
        all_todo = graphene.List(TODOType)
    
        def resolve_all_users(root, info):
            return User.objects.all()
    
        def resolve_all_project(root, info):
            return Project.objects.all()
    
        def resolve_all_todo(root, info):
            return TODO.objects.all()

#### Создадим объект схемы графена.
    schema = graphene.Schema(query=Query)

## Последовательность действий tasks lesson-11

Последовательность действий
1. В проекте добавить возможность создавать и удалять проекты. done
2. Добавить возможность создавать и удалять ToDo. done
3. Добавить поиск по части названия проекта.
4. Все запросы на сервер рекомендуется делать в главном приложении.
5. Для взаимодействия с главным приложением передавать callback.
6. * Добавить возможность изменять проекты.


## Создание и удаление проектов. 
Создаем файл ProjectForm.js

    import React from 'react'
    
    
    class ProjectForm extends React.Component {
      constructor(props) {
        super(props);
        this.state = {
        title: '',
        linkGitHub: '',
        users: []
        }
      }
    
      handleChange(event) {
        this.setState({
        [event.target.name]: event.target.value
        })
      }
    
      handleUserChange(event) {
          if (!event.target.selectedOptions) {
              this.setState({
                  'users': []
                })
                return;
          }
          let users = []
          for(let i = 0; i < event.target.selectedOptions.length;i++){
                users.push(event.target.selectedOptions.item(i).value)
            }
            this.setState(
                {'users':users}
            )
      }
    
      handleSubmit(event) {
        this.props.create_project(this.state.title, this.state.linkGitHub, this.state.users)
        event.preventDefault();
      }
    
      render() {
        return (
          <form onSubmit={(event) => this.handleSubmit(event)}>
            <br></br>
    
            <label for="title">Проект
                <div>
                  <input type="text" name="title" value={this.state.title}
                  onChange={(event) => this.handleChange(event)}/>
                </div>
            </label>
    
            <label for="linkGitHub">GitHub
                <div>
                  <input type="text" name="linkGitHub" value={this.state.linkGitHub}
                   onChange={(event) => this.handleChange(event)}/>
                </div>
            </label>
    
            <br></br>
            <label for="users">Авторы
                 <div>
                    <select name="users" multiple
                        onChange={(event) => this.handleUserChange(event)}>
                        {this.props.users.map((item) => <option
                        value={item.id}>{item.last_name}</option>)}
                    </select>
                </div>
            </label>
            <br></br>
            <input type="submit" value="Сохранить" />
          </form>
        );
      }
    }
    
    export default ProjectForm

Вносим корректировки в файл App.js
загружаем компонент

    ...
    import ProjectForm from "./components/ProjectForm";
    ...
    delete_project(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers, headers})
        .then(response => {
        this.setState({projects: this.state.projects.filter((project)=>project.id !==
        id)})
        }).catch(error => console.log(error))
    }

    create_project(title, linkGitHub, users) {
        const headers = this.get_headers()
        const data = {title: title, linkGitHub: linkGitHub, users: users}
        axios.post(`http://127.0.0.1:8000/api/projects/`,data,{headers})
        .then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }
    ...
    <Route exact path='/projects/create' element={<ProjectForm users={this.state.users} create_project={(title,linkGitHub,users) => this.create_project(title,linkGitHub,users)}/>}/>

## Создание и удаление ToDo App.js. 

    ...
    deleteToDo(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers, headers})
        .then(response => {
        this.setState({todos: this.state.todos.filter((todo)=>todo.id !==
        id)})
        }).catch(error => console.log(error))
    }
    ...

## Сборка проекта 

Установите реагирующие скрипты с помощью следующей команды:

    npm install react-scripts

Установите зависимости с помощью следующей команды:

    npm install

Запустите локальный сервер, выполнив следующую команду:

    npm run start


The project was built assuming it is hosted at the server root.
You can control this with the homepage field in your package.json.
For example, add this to build it for GitHub Pages:

  "homepage" : "http://myname.github.io/myapp",

The build folder is ready to be deployed.
You may serve it with a static server:

  npm install -g serve
  serve -s build

Find out more about deployment here:

  https://bit.ly/CRA-deploy


для запуска 

    docker ps -a

Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:  ....

Запустить следующую команду

    sudo chmod 666 /var/run/docker.sock

Проверить занятые порты

    sudo netstat -tulpn | grep LISTEN

tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      1205/postgres    

Освободить занятый порт

     sudo kill -9 1205

docker-compose -f docker-compose.yml -a

Изменить запуск сервера через gunicorn, для этого добавим в файл docker-compose.yml 
следующую строчку:
    
    && gunicorn GB_TODO_notes_v2.wsgi -b 0.0.0.0:8080

В файле Dockerfile добавим следующую строчку:

    RUN pip install gunicorn

И перезапустим сервер 

    docker-compose -f docker-compose.yml up -d

Ошибка

Пересобираем весь контейнер:

    docker-compose -f docker-compose.yml up -d --build


Смотреть логи

    docker logs

Сбросить сервер

    docker-compose -f docker-compose.yml down
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

### Последовательность действий tasks lesson-2

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

### Последовательность действий tasks lesson-3
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

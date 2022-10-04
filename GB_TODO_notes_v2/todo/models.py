from django.db import models

from users.models import User


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=24, blank=True, help_text='Заголовок проекта')
    linkGitHub = models.URLField(max_length=200, null=True, blank=True, help_text='Ссылка на репозиторий GitHub')
    users = models.ManyToManyField(User)


class TODO(models.Model):
    STATUS_CHOICES = [
        ('a', 'active'),
        ('с', 'closed'),
    ]
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True, help_text='поле для заметок')
    create_publish = models.DateField(auto_now_add=True, help_text='поле даты создания заметки')
    update_publish = models.DateField(auto_now=True, help_text='поле даты обновления заметки')
    users = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, help_text='поля авто заметки')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, help_text='поле статуса,активная или закрыта')

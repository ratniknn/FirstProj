from django.db import models


class UserList(models.Model):
    id_user = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_access = models.BooleanField(default=True, verbose_name="Доступ разрешен")
    id_level = models.ForeignKey('UserLevel', on_delete=models.PROTECT, verbose_name="Уровень доступа")


class UserLevel(models.Model):
    id_level = models.AutoField(primary_key=True)
    level = models.IntegerField(max_length=3, verbose_name="Уровень доступа")
    discriptions = models.TextField(max_length=100, verbose_name="Наименование доступа")
    create = models.BooleanField(default=False, verbose_name="Создание нового")
    read = models.BooleanField(default=False, verbose_name="Чтение")
    edit = models.BooleanField(default=False, verbose_name="Изменение")
    deletion = models.BooleanField(default=False, verbose_name="Удаление")



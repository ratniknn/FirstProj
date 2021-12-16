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
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

class Specialist(models.Model):
    id_spec = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('UserList', on_delete=models.PROTECT, verbose_name='ID user')
    spec_name = models.TextField(max_length=100, verbose_name='Имя')
    spec_surname = models.TextField(max_length=100, verbose_name='Фамилия')
    position = models.TextField(max_length=255, verbose_name='Должность')
    mail = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class Contractor(models.Model):
    id_contractor = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('UserList', on_delete=models.PROTECT, verbose_name='ID user')
    contractor_name = models.TextField(max_length=255, verbose_name='Наиманование организации')
    mail = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class MallList(models.Model):
    id = models.AutoField(primary_key=True)
    number_mall = models.IntegerField(max_length=5, verbose_name='Номер магазина')
    city = models.TextField(max_length=100, verbose_name='Город')
    address = models.TextField(max_length=255, verbose_name='Адрес')
    mall = models.TextField(max_length=255, verbose_name='Торговый центр')
    director = models.TextField(max_length=100, verbose_name='Директор')
    id_spec = models.ForeignKey('Specialist', on_delete=models.PROTECT, verbose_name='Специалист')
    business = models.TextField(max_length=100, verbose_name='Бизнес')
    brand = models.TextField(max_length=100, verbose_name='Брэнд')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class UserMall(models.Model):
    id_user_mall = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('UserList', on_delete=models.PROTECT, verbose_name='ID user')
    user_name = models.TextField(max_length=100, verbose_name='Имя')
    user_surname = models.TextField(max_length=100, verbose_name='Фамилия')
    position = models.TextField(max_length=255, verbose_name='Должность')
    mail = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class TaskInWork(models.Model):
    id_task = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('UserList', on_delete=models.PROTECT, verbose_name='Пользователь')
    id_mall = models.ForeignKey('MallList', on_delete=models.PROTECT, verbose_name='Магазин')
    system = models.TextField(max_length=255, verbose_name='Тип системы')
    text_fault = models.TextField(max_length=500, verbose_name='Описание проблемы')
    problem_solution = models.TextField(max_length=500, verbose_name='Решение по проблеме')
    in_work = models.BooleanField(default=False, verbose_name='Заявка в работе')
    done = models.BooleanField(default=False, verbose_name='Заявка выполнена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")




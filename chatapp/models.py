import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserDetail(models.Model):
    birth_month = models.IntegerField('birth month', default=None, null=True, blank=True)
    birth_year = models.IntegerField('birth year', default=None, null=True, blank=True)
    update_date = models.DateTimeField('updated date', auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.user.username


class OnePlace(models.Model):
    name = models.CharField('Illness name', max_length=200, unique=True)
    description = models.TextField('description', max_length=1000, null=True)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)

    def __str__(self):
        return self.name


class UserOnePlace(models.Model):
    oneplace = models.ForeignKey(OnePlace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cured_date = models.DateTimeField('cured date', null=True, blank=True, default=None)
    add_date = models.DateTimeField('add date', auto_now_add=True)
    update_date = models.DateTimeField('updated date',  auto_now=True)

    def __str__(self):
        return self.illness.name
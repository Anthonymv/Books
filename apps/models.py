import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Register(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    number_credits = models.IntegerField()

    def __str__(self):
        return u'{}'.format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_student = models.ManyToManyField(Subject)

    def full_name(self):
        return u'{} {}'.format(self.name, self.last_name)


class Books(models.Model):
    title = models.CharField(max_length=150, )
    sub_title = models.CharField(max_length=100, )
    author = models.CharField(max_length=100, )
    description = models.TextField(max_length=800, )
    content = models.TextField(max_length=2000, )
    date_created = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return u'{}'.format(self.title)

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


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
    date_created = models.DateTimeField(default=timezone.now, )
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return u'{}'.format(self.title)

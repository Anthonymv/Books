from django.db import models


# Create your models here.

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
    title = models.CharField(max_length=150)
    contenido = models.TextField()

    def __str__(self):
        return u'{}'.format(self.title)

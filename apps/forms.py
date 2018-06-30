from django import forms
from django.contrib.auth.models import User

from apps.models import Student, Books, Register


# User Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_student': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}, ),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.DateInput(attrs={'class': 'form-control'}),
        }

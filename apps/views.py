from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView

from apps.models import Student, Books, Register
from apps.forms import StudentForm, BooksForm, RegisterForm


# Create your views here.

@login_required
def index(request):
    return render(request, template_name='index.html')


def list_student(request):
    student = Student.objects.all()
    return render(request, template_name='list_student.html', context={'student': student})


class RegisterUser(FormView):
    model = Register
    form_class = RegisterForm
    template_name = 'user/login/register.html'


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_success_url(self):
        return reverse('list_student')


class StudentEdit(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'

    def get_success_url(self):
        return reverse('list_student')


class StudentDelete(DeleteView):
    model = Student
    form_class = StudentForm
    template_name = 'delete_student.html'

    def get_context_data(self, **kwargs):
        context_data = super(StudentDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = Student.objects.get(id=int(pk))
        context_data.update({'student': student})
        return context_data

    def get_success_url(self):
        return reverse('list_student')


class BooksList(ListView):
    model = Books
    template_name = 'books/books.html'


class BooksDetail(DetailView):
    model = Books
    template_name = 'books/books_view.html'


class BooksDelete(DeleteView):
    model = Books
    form_class = BooksForm
    template_name = 'books/books_delete.html'

    def get_context_data(self, **kwargs):
        context_data = super(BooksDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        book = Student.objects.get(id=int(pk))
        context_data.update({'book': book})
        return context_data

    def get_success_url(self):
        return reverse('book_list')


class BooksCreate(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'books/books_add.html'

    def get_success_url(self):
        return reverse('book_list')


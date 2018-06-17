from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.models import Student, Books
from apps.forms import StudentForm


# Create your views here.

@login_required
def index(request):
    return render(request, template_name='index.html')


def list_student(request):
    student = Student.objects.all()
    return render(request, template_name='list_student.html', context={'student': student})


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


class BookDjango(ListView):
    template_name = 'books/book_django.html'
    model = Books
    pass

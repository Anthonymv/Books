from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_student/', views.list_student, name='list_student'),
    path('create_student/', views.StudentCreate.as_view(), name='create_student'),
    path('book_django/', views.BookDjango.as_view(), name='book_django'),
    re_path(r'^edit_student/(?P<pk>\d+)/$', views.StudentEdit.as_view(), name='edit_student'),
    re_path(r'^delete_student/(?P<pk>\d+)/$', views.StudentDelete.as_view(), name='delete_student'),
]
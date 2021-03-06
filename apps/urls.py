from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/list/', views.list_student, name='list_student'),
    path('student/create/', views.StudentCreate.as_view(), name='create_student'),
    re_path(r'^student/edit/(?P<pk>\d+)/$', views.StudentEdit.as_view(), name='edit_student'),
    re_path(r'^student/delete/(?P<pk>\d+)/$', views.StudentDelete.as_view(), name='delete_student'),

    path('register/user/', views.RegisterUser.as_view(), name='register_user'),
    path('book/list/', views.BooksList.as_view(), name='book_list'),
    path('book/create/', views.BooksCreate.as_view(), name='book_create'),
    re_path(r'^book/view/(?P<pk>\d+)/$', views.BooksDetail.as_view(), name='book_view'),
    re_path(r'^book/delete/(?P<pk>\d+)/$', views.BooksDelete.as_view(), name='book_delete'),
]

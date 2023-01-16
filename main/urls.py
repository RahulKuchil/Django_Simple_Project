from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('edit_confirm/<int:id>/', views.edit_confirm, name='edit_confirm'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_confirm/', views.add_confirm, name='add_confirm'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/create-user/', views.UserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('user-process/', views.UserProcessList.as_view()),
    path('user-process/<int:pk>/', views.UserProcessList.as_view()),
]
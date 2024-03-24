from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/create-event/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('eventmentors/', views.EventMentorList.as_view()),
    path('eventmentors/<int:pk>/', views.EventMentorDetail.as_view()),
]

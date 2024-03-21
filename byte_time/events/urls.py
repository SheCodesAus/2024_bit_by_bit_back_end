from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/create-event/', views.CreateEvent.as_view()),
]

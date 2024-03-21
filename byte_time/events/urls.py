from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/create-event/', views.EventList.as_view()),
]

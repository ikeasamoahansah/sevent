from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="event"),
    path('add/', views.add_event, name="add_event"),
    path('event/<uuid:event_id>/', views.view_event, name='view_event'),
    path('event/<uuid:event_id>/register', views.register_event, name="register_event")
]

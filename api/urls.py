from django.urls import path
from . import views

urlpatterns = [
    path('insert-hello-world/', views.insert_hello_world, name='insert_hello_world'),  # POST endpoint
    path('fetch-hello-world/', views.fetch_hello_world, name='fetch_hello_world'),  # GET endpoint
]

from django.urls import path
from .views import CreateTaskView, home

urlpatterns = [
    path('', home, name='home'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
]
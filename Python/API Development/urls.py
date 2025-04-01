from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task_details'),
    path('api/token/', obtain_auth_token, name='api_token_auth'), # Token generation endpoint
]
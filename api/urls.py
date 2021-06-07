from django.urls import path
from .views import TaskView, TaskCreate, TaskDetail, TaskUpdate,  TaskDelete

urlpatterns = [
    path('getall/', TaskView.as_view(), name="task-list"),
    path('get/<str:pk>/', TaskDetail.as_view(), name="task-detail"),
    path('create/', TaskCreate.as_view(), name="task-create"),
    path('put/<str:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('delete/<str:pk>/', TaskDelete.as_view(), name="task-delete"),
]

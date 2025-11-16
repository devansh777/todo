from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('completeTask/<int:pk>',views.completeTask,name='completeTask'),
    path('incomplatedTask/<int:pk>',views.incomplatedTask,name='incomplatedTask'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask'),
    #Edit task
    path('editTask/<int:pk>',views.editTask,name='editTask'),
    path('saveTask',views.saveTask,name="saveTask"),
]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.getUsers),
#     path('create', views.addUser),
#     path('read/<str:pk>', views.getUser),
#     path('update/<str:pk>', views.updateUser),
#     path('delete/<str:pk>', views.deleteUser),
# ]

from django.urls import path
from .views import getUsers, getUser, addUser, updateUser, deleteUser, getAdmin, getTrainer, getClient, login
from .views import getTrainerNames, addSchedule
urlpatterns = [
    path('', getUsers),
    path('<int:pk>/', getUser),
    path('register', addUser),
    path('update/<int:pk>', updateUser),
    path('delete/<int:pk>', deleteUser),
    path('admin', getAdmin),
    path('trainer', getTrainer),
    path('client', getClient),
    path('login', login),
    path('getTrainerInfo', getTrainerNames),
    path('addSchedule', addSchedule)
]

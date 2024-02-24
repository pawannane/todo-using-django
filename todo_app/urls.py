from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name="logout"),
    path('update-todo/<str:id>/', update_todo, name="update_todo"),
    path('delete-todo/<str:id>/', delete_todo, name="delete_todo"),
]

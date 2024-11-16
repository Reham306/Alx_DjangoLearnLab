from django.urls import path
from .views import register, user_login, user_logout, list_books

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("books/", list_books, name="list_books"),
]

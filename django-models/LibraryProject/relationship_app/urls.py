from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),  # Use custom register view
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),  # Use Django's built-in LoginView with custom template
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),  # Use Django's built-in LogoutView with custom template
    path("books/", views.list_books, name="list_books"),  # Function-based view for books
]

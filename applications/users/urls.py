from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        "register/", 
        views.UserRegisterView.as_view(), 
        name="register",
    ),
    path(
        "login2/", 
        views.LoginUser.as_view(), 
        name="user-login",
    ),
    path(
        "logout2/", 
        views.LogoutView.as_view(), 
        name="user-logout",
    ),
    path(
        'auth/',
        views.CustomAuthToken.as_view(),
    ),
]
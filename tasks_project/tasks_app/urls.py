from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("user/", views.user_account, name="user_account"),
    path("add-task/", views.add_task, name="add_task"),
]
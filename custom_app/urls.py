from django.urls import path
from custom_app import views
from django.contrib.auth.decorators import login_required


app_name = "custom_app"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("login_page/", views.LoginPageView.as_view(), name="login_page"),
    path("successful_login/", login_required(views.SuccessfulLoginView.as_view()), name="successful_login"),
    path("register/", views.Registration.as_view(), name="registration"),
    path("forget_password_page/", views.ForgetPasswordView.as_view(), name="forget_password_page"),
]
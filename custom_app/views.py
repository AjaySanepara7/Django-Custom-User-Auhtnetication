from django.urls import reverse
from django.conf import settings
from custom_app.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from custom_app.forms import CustomUserForm
from django.views import View


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "custom_app/home.html")
    

class Registration(View):
    user_form_class = CustomUserForm
    template_name = "custom_app/registration.html"

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class()
        return render(request, self.template_name, {"user_form": user_form})
    
    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST)
        if user_form.is_valid():
            user_form.save()

            return HttpResponseRedirect(reverse("custom_app:login_page"))
        
        return render(request, self.template_name, {"user_form": user_form})
    

class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "custom_app/login_page.html")
    
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("custom_app:successful_login"))
        else:
            context = {
                "login_failed": "Login failed. Invalid credentials"
            }
            return render(request, "custom_app/login_page.html", context)
        

class SuccessfulLoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "user": request.user,
        }
        return render(request, "custom_app/successful_login.html", context)
    
    def post(self, request, *args, **kwargs):
        logout(request)
        context = {
                "logout": "Logout Successful"
            }
        return render(request, "custom_app/login_page.html", context)
    

class ForgetPasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "custom_app/forget_password_page.html")
    
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.check_password(request.POST.get("current_password")):
            if user.check_password(request.POST.get("password")):
                context = {
                "same_password": "The new password cannot be the same as the current password"
                }
                return render(request, "custom_app/forget_password_page.html", context)
            else:
                user.set_password(request.POST.get("password"))
                user.save()
                context = {
                "success_change_password": "Password changed successfully"
                }
                return render(request, "custom_app/forget_password_page.html", context)
        else:
            context = {
            "fail_change_password": "Invalid Password"
            }
            return render(request, "custom_app/forget_password_page.html", context) 


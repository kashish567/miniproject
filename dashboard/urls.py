"""interviewprep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register,login_user,logout_user
urlpatterns = [
    path('', home,name="home"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path("register/", register, name="register"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user/", logout_user, name="logout_user"),
]
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
from . views import *
urlpatterns = [
    path('', home,name="home"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path("register/", register, name="register"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user/", logout_user, name="logout_user"),
    path("add_que/", addIntQues, name="add_que"),
    path("add_catg/",addCatg,name="add_catg"),
    path("addAns/",addAns,name="add_Ans"),
    path("displayQues/",displayQues,name="disQues"),
    path("getAns/<int:pk>/",getAns,name = "getAns"),
    path("searchRecmd/",searchRecmd,name="searchRcmd"),
    path("search/",searchQuest,name = "search"),

    # path("dislay_que/", display_que , name="display_que"),
]
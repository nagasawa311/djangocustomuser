from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("log_out",views.log_out,name="log_out"),
    path("list",views.list,name="list"),
    path("delete",views.delete,name="delete"),
]

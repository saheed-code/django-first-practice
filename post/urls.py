from django.urls import path
from . import views

urlpatterns = {
    path("hello/", views.hello, name="hello"),
    path("greet/", views.greet, name="greet"),
    path("work/", views.work, name="work")
}
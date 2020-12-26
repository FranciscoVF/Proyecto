from django.urls import path

from apps.general import views

app_name = "paginas"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]

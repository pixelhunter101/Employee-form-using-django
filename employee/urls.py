from django.urls import path
from . import views
urlpatterns = [
    path('', views.form),
    path('info', views.info)
]
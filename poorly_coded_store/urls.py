from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/buying_process', views.buying_process),
    path('<int:id>/checkout', views.checkout)
]

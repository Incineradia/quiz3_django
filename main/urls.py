from django.urls import path
from . import views
urlpatterns=[
    path('main/', views.SomethingClass.as_view(), name="main"),
]
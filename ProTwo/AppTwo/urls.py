from django.urls import path
from AppTwo import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.users, name="users"),
]

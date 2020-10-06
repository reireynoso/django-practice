from django.urls import path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="list"),
    path("<slug:pk>/", views.SchoolDetailView.as_view(),name="detail")
]
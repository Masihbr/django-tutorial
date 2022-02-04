from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    # path("", views.homeView, name="home"),  # for regular view
]

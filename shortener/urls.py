
from django.urls import path
from . import views

urlpatterns = [
    path("shorten/", views.CreateShortURL.as_view(), name="shorten"),
    path("<str:code>/", views.RedirectURL.as_view(), name="redirect"),
]
from django.urls import path
from .views import home, about, contacts, delivery

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("delivery/", delivery, name="delivery"),
]

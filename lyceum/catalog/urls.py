from django.urls import path
from catalog import views

urlpatterns = [
    path("", views.hi, name="hi", kwargs={"name": "Cупер Эндик"}),
]

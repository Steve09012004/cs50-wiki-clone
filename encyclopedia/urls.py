from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path('add', views.add, name="add"),
    path('edit/<str:name>', views.edit, name="edit"),
    path("<str:name>", views.view, name="view")
]

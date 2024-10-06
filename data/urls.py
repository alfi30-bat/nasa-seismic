
from django.urls import path

from . import views

app_name = "data"
urlpatterns = [
    path("moon/", views.moon_data, name="moon"),
    path("mars/", views.mars_data, name="mars"),
    path("", views.index, name="home"),
    path("features/", views.features, name="features"),

]
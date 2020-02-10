from django.conf.urls import include, url
from .views import home

app_name = "landing"
urlpatterns = (
    url(r"", home, name="home")
)

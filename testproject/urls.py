from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path
from landing.views import home
from dashboard.urls import dashboard, create_user, dash, sign_in


urlpatterns = (
    url(r"^admin/", admin.site.urls),
    url(r"^api/auth/", include("djoser.urls.base")),
    url(r"^api/auth/", include("djoser.urls.authtoken")),
    url(r"^api/auth/", include("djoser.urls.jwt")),
    url(r"^api/auth/", include("djoser.social.urls")),

    path("", home, name="home"),
    url(r"^account/login", dashboard, name="login"),
    url(r"^account/register", create_user, name="register"),
    url(r"^dashboard", dash, name="dashbaord"),
    url(r"^login", sign_in, name="signin"),
    #url(r'^', include('landing.urls')),
)
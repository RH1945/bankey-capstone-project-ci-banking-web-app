from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "bankey_account"

urlpatterns = [
    path("", include("views.account_view")),
    path("admin/", admin.site.urls),
    path("statement/", include("vies.statement.urls")),
]

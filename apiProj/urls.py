from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apiApp.urls')),
]


# http://127.0.0.1:8000/api/hello?visitor_name=John
# visit this url to get a visitor's name
# name in the url can be changed
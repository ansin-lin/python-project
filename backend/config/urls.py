from django.contrib import admin
from django.urls import path
from words.views import words_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/words/", words_api),
]

from django.contrib import admin
from django.template.context_processors import static
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include('agriapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

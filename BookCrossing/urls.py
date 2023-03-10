from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/chat/', include('Chat.urls')),
    path('api/v1/profile/', include('Profile.urls')),
    path('api/v1/book/', include('Book.urls')),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]


urlpatterns += doc_urls

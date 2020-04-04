
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('entries/', include('entries.urls')),
    path('users/', include('users.urls')),
]

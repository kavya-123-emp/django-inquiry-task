from django.urls import include
from django.contrib import admin
from django.urls import path, include  # ✅ include is needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # ✅ this connects your app's URLs
]

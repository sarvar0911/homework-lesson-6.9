from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('themes/', include('Themes.urls')),
    path('students/', include('Students.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('outcomes/', include('outcomes.urls')),
    path('tasks/', include('tasks.urls')),
]

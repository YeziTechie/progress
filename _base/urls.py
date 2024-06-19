from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('outcomes.urls')),
    path('outcomes/', include('outcomes.urls')),
    path('tasks/', include('tasks.urls')),
    path('user/', include('user.urls')),
]

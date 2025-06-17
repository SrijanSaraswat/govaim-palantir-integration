from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/connections/', include('connections.urls')),
    path('api/analyses/', include('analyses.urls')),
    path('api/workflows/', include('workflows.urls')),
    path('api/chat/', include('govaim_chat.urls')),
]

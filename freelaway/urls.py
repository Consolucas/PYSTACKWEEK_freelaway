from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', include ('autenticacao.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('jobs/', include('jobs.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
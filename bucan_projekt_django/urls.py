from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genshin/', include('genshin.urls')),
    path('', RedirectView.as_view(url='genshin/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

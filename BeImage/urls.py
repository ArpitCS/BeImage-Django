from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from app.views import toggle_favorite, favorites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('toggle_favorite/<int:pk>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', favorites, name='favorites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
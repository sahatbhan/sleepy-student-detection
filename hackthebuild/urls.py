from django.contrib import admin
from django.urls import path
from api import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('live', views.Live, name='live-video'),
    path('weekly', views.Allstats, name='weekly-stats'),
    path('daily', views.Dailystats, name='daily-stats'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

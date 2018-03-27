from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from hmt import views

router = routers.DefaultRouter()
router.register(r'event_types', views.EventTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('hmt.urls', namespace='hmt')),
    url('api/', include((router.urls, 'api'))),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

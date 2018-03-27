from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from hmt import views
from hmt.views import EventCreateView, EventTypeCreateView, EventTypesListView

urlpatterns = [
    path('', EventTypesListView.as_view()),
    path('admin/', admin.site.urls),
    path('add_new_event_type/', EventTypeCreateView.as_view()),
    path('add_new_event/', views.create_event)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

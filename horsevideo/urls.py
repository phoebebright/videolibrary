from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.conf.urls import url
from web.views import LibraryListView

urlpatterns = [
    url(r'^$', LibraryListView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    ]


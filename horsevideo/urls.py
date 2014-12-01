from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.conf.urls import url
from web.views import LibraryListView, LibraryAddView, LibraryDisplayView

urlpatterns = [
    url(r'^$', LibraryListView.as_view()),
    url(r'^add/$', LibraryAddView.as_view(), name="add"),
    url(r'^list/$', LibraryListView.as_view(), name="list"),
    url(r'^view/?P<id>\w+/$', LibraryDisplayView.as_view(), name="view"),

    url(r'^admin/', include(admin.site.urls)),
    ]


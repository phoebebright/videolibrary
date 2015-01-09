from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from web.views import LibraryListView, LibraryAddView, LibraryDisplayView

urlpatterns = [
    url(r'^$', LibraryListView.as_view()),
    url(r'^add/$', LibraryAddView.as_view(), name="add"),
    url(r'^list/$', LibraryListView.as_view(), name="list"),
    url(r'^view/(?P<pk>\d+)/$', LibraryDisplayView.as_view(), name="view"),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




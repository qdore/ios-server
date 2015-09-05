from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^weixin2py/', include('weixin2py.foo.urls')),
    # url(r'^', include(admin.site.urls)),
    url(r'^ios/',include("ios.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

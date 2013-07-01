from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'photoplanet.views.home', name='home'),
    # url(r'^photoplanet/', include('photoplanet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(
        r'^all/',
        TemplateView.as_view(template_name="photoplanet/all.html"),
        name='all'),
    url(r'^about/', 'photoplanet.views.about', name='about'),
    url(r'^login/', 'photoplanet.views.login', name='login'),
    url(r'^day/', 'photoplanet.views.day', name='day'),

    url(r'^feedback/', include('feedback.urls'))
)

# add static from Artem repo
urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
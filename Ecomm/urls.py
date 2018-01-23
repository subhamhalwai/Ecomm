from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from ecommapp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'Ecomm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home, name='home'),
    url(r'^about/',views.about, name='about'),
    url(r'^profile/',views.userProfile, name='profile'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^checkout/',views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
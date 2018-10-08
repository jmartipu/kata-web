from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'buscoayuda4101.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('kata.urls', namespace="principal")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/', include('django.contrib.auth.urls'))
]
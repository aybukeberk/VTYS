from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Otel_Sitesi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^loginapp/$', 'django.contrib.auth.views.login'),
    url(r'^loginapp/logout/$', logout_page),
    url(r'^loginapp/accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^loginapp/register/$', register),
    url(r'^loginapp/register/success/$', register_success),
    url(r'^loginapp/home/$', home),
)






LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'

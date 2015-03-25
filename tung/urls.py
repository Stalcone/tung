from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns(
    '',
    url(r'^colls/', include('colls.urls', namespace='colls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', views.SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogOutView.as_view(), name='logout'),
)

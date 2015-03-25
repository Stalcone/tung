from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.CollListView.as_view(), name='index'),
    url(r'^coll(?P<pk>\d+)/$', views.CollDetailView.as_view(),
        name='coll_detail'),
    url(r'^coll(?P<pk>\d+)/(?P<year>\d{4})/$', views.CollYearView.as_view(),
        name='coll_year'),
    url(r'^create/$', views.CollCreateView.as_view(), name='coll_create'),
    url(r'^coll(?P<pk>\d+)/edit/$', views.CollUpdateView.as_view(),
        name='coll_edit'),
    url(r'^coll(?P<pk>\d+)/delete/$', views.CollDeleteView.as_view(),
        name='coll_delete'),
    url(r'^item(?P<pk>\d+)/$', views.ItemDetailView.as_view(),
        name='item_detail'),
    url(r'^coll(?P<pk>\d+)/add/$', views.ItemCreateView.as_view(),
        name='item_create'),
    url(r'^item(?P<pk>\d+)/edit/$', views.ItemUpdateView.as_view(),
        name='item_edit'),
    url(r'^item(?P<pk>\d+)/delete/$', views.ItemDeleteView.as_view(),
        name='item_delete'),
)

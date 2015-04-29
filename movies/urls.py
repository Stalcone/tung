from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^movie_index/$', views.MovieListView.as_view(), name='movie_list'),
    url(r'^movie(?P<pk>\d+)/$', views.MovieDetailView.as_view(),
        name='movie_detail'),
    url(r'^add_movie$', views.MovieCreateView.as_view(), name='movie_create'),
    url(r'^movie(?P<pk>\d+)/edit/$', views.MovieUpdateView.as_view(),
        name='movie_update'),
    url(r'^movie(?P<pk>\d+)/delete/$', views.MovieDeleteView.as_view(),
        name='movie_delete'),

    url(r'^tv_index/$', views.TVShowListView.as_view(), name='tvshow_list'),
    url(r'^tv(?P<pk>\d+)/$', views.TVShowDetailView.as_view(),
        name='tvshow_detail'),
    url(r'^add_tv$', views.TVShowCreateView.as_view(),
        name='tvshow_create'),
    url(r'^tv(?P<pk>\d+)/edit/$', views.TVShowUpdateView.as_view(),
        name='tvshow_update'),
    url(r'^tv(?P<pk>\d+)/delete/$', views.TVShowDeleteView.as_view(),
        name='tvshow_delete'),

    url(r'^tv(?P<pk>\d+)/s(?P<number>\d+)/$',
        views.TVShowSeasonDetailView.as_view(), name='tvshow_season_detail'),
    url(r'^tv(?P<pk>\d+)/add_season/$', views.TVShowSeasonCreateView.as_view(),
        name='tvshow_season_create'),
    url(r'^tv(?P<pk>\d+)/s(?P<number>\d+)/edit/$',
        views.TVShowSeasonUpdateView.as_view(),
        name='tvshow_season_update'),
    url(r'^tv(?P<pk>\d+)/s(?P<number>\d+)/delete/$',
        views.TVShowSeasonDeleteView.as_view(),
        name='tvshow_season_delete'),

    url(r'person_index', views.PersonListView.as_view(), name='person_list'),
    url(r'^person(?P<pk>\d+)/$', views.PersonDetailView.as_view(),
        name='person_detail'),
    url(r'^person(?P<pk>\d+)/delete$', views.PersonDeleteView.as_view(),
        name='person_delete'),

    url(r'^genres/$', views.GenreListView.as_view(), name='genre_list'),
    url(r'^genre/$', views.GenreDetailView.as_view(), name='genre_detail'),

    url(r'^years/$', views.YearListView.as_view(), name='year_list'),
    url(r'^year/$', views.YearDetailView.as_view(), name='year_detail'),
)

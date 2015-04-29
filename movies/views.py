from string import ascii_uppercase

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from braces import views

from . import forms, models


class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class IndexView(
    RestrictToUserMixin,
    generic.TemplateView
):
    template_name = 'movies/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        movies = models.Movie.objects.filter(user=self.request.user)
        last_movies = movies.order_by('-date_added')[:5]
        context['last_movies'] = last_movies

        movies = movies.all()
        movie_letters = []
        for letter in ascii_uppercase:
            for movie in movies:
                if (movie.first_letter == letter and
                        letter not in movie_letters):
                    movie_letters.append(letter)
                    break
        context['movie_letters'] = movie_letters

        persons = models.Person.objects.filter(user=self.request.user)
        russian_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
        person_letters = []
        for letter in russian_letters:
            for person in persons:
                if (person.first_letter == letter and
                        letter not in person_letters):
                    person_letters.append(letter)
                    break
        context['person_letters'] = person_letters

        return context


class MovieListView(
    RestrictToUserMixin,
    generic.ListView
):
    model = models.Movie

    def get_queryset(self):
        queryset = super(MovieListView, self).get_queryset()
        letter = self.request.GET.get('letter', '')
        if letter:
            queryset = queryset.filter(first_letter=letter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        letter = self.request.GET.get('letter', '')
        context['letter'] = letter

        movies = models.Movie.objects.filter(user=self.request.user)
        movies = movies.all()
        movie_letters = []
        for letter in ascii_uppercase:
            for movie in movies:
                if (movie.first_letter == letter and
                        letter not in movie_letters):
                    movie_letters.append(letter)
                    break
        context['movie_letters'] = movie_letters

        return context


class MovieDetailView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.Movie


class MovieCreateView(
    views.LoginRequiredMixin,
    generic.CreateView
):
    form_class = forms.MovieForm
    model = models.Movie

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.set_first_letter()
        self.object.save()
        director_name = form.cleaned_data['director_list'].split(', ')
        for name in director_name:
            try:
                director = models.Person.objects.get(name=name,
                                                     user=self.request.user)
            except ObjectDoesNotExist:
                director = models.Person(name=name, user=self.request.user)
                director.set_first_letter()
                director.save()
            director.directed.add(self.object)

        actors_name = form.cleaned_data['actors_list'].split(', ')
        for name in actors_name:
            try:
                actor = models.Person.objects.get(name=name,
                                                  user=self.request.user)
            except ObjectDoesNotExist:
                actor = models.Person(name=name, user=self.request.user)
                actor.set_first_letter()
                actor.save()
            actor.starred_in.add(self.object)
        return super(MovieCreateView, self).form_valid(form)


class MovieUpdateView(
    RestrictToUserMixin,
    generic.UpdateView
):
    form_class = forms.MovieForm
    model = models.Movie

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_first_letter()
        self.object.save()

        # First we will delete this movie from all the
        # directors and actors it's assotiatied with.
        # Then we will create new bonds.

        for director in self.object.director.all():
            director.directed.remove(self.object)

        for actor in self.object.actors.all():
            actor.starred_in.remove(self.object)

        director_name = form.cleaned_data['director_list'].split(', ')
        for name in director_name:
            try:
                director = models.Person.objects.get(name=name,
                                                     user=self.request.user)
            except ObjectDoesNotExist:
                director = models.Person(name=name, user=self.request.user)
                director.set_first_letter()
                director.save()
            director.directed.add(self.object)

        actors_name = form.cleaned_data['actors_list'].split(', ')
        for name in actors_name:
            try:
                actor = models.Person.objects.get(name=name,
                                                  user=self.request.user)
            except ObjectDoesNotExist:
                actor = models.Person(name=name, user=self.request.user)
                actor.set_first_letter()
                actor.save()
            actor.starred_in.add(self.object)
        return super(MovieUpdateView, self).form_valid(form)


class MovieDeleteView(
    RestrictToUserMixin,
    views.MessageMixin,
    generic.DeleteView
):
    model = models.Movie
    success_url = reverse_lazy('movies:index')


class TVShowListView(
    RestrictToUserMixin,
    generic.ListView
):
    model = models.TVShow

    def get_context_data(self, **kwargs):
        context = super(TVShowListView, self).get_context_data(**kwargs)
        drama = models.TVShow.objects.filter(genre='драма')
        comedy = models.TVShow.objects.filter(genre='комедия')
        sci_fi = models.TVShow.objects.filter(genre='фантастика')
        animation = models.TVShow.objects.filter(genre='анимация')
        context['drama'] = drama.all()
        context['comedy'] = comedy.all()
        context['sci_fi'] = sci_fi.all()
        context['animation'] = animation.all()
        return context


class TVShowDetailView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.TVShow

    def get_context_data(self, **kwargs):
        context = super(TVShowDetailView, self).get_context_data(**kwargs)
        seasons = models.TVShowSeason.objects.filter(user=self.request.user,
                                                     tvshow=self.get_object())
        seasons = seasons.order_by('number')
        context['seasons'] = seasons
        return context


class TVShowCreateView(
    views.LoginRequiredMixin,
    generic.CreateView
):
    form_class = forms.TVShowForm
    model = models.TVShow

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        creator_name = form.cleaned_data['creator_list'].split(', ')
        for name in creator_name:
            try:
                creator = models.Person.objects.get(name=name,
                                                    user=self.request.user)
            except ObjectDoesNotExist:
                creator = models.Person(name=name, user=self.request.user)
                creator.set_first_letter()
                creator.save()
            creator.created.add(self.object)
        return super(TVShowCreateView, self).form_valid(form)


class TVShowUpdateView(
    RestrictToUserMixin,
    generic.UpdateView
):
    form_class = forms.TVShowForm
    model = models.TVShow

    def form_valid(self, form):
        self.object = form.save()

        # First we will delete this movie from all the
        # creators it's assotiatied with.
        # Then we will create new bonds.

        for creator in self.object.creator.all():
            creator.created.remove(self.object)

        creator_name = form.cleaned_data['creator_list'].split(', ')
        for name in creator_name:
            try:
                creator = models.Person.objects.get(name=name,
                                                    user=self.request.user)
            except ObjectDoesNotExist:
                creator = models.Person(name=name, user=self.request.user)
                creator.set_first_letter()
                creator.save()
            creator.created.add(self.object)
        return super(TVShowUpdateView, self).form_valid(form)


class TVShowDeleteView(
    RestrictToUserMixin,
    generic.DeleteView
):
    model = models.TVShow
    success_url = reverse_lazy('movies:tvshow_list')


class TVShowSeasonDetailView2(
    RestrictToUserMixin,
    generic.TemplateView
):
    template_name = 'movies/tvshowseason_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TVShowSeasonDetailView2, self).get_context_data(
            **kwargs)
        tvshow = get_object_or_404(models.TVShow, pk=self.kwargs['pk'])
        number = self.kwargs['number']
        season = models.TVShowSeason.objects.get(tvshow=tvshow,
                                                 number=number)
        context['season'] = season
        return context


class TVShowSeasonDetailView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.TVShowSeason

    def get_object(self):
        tvshow = get_object_or_404(models.TVShow, pk=self.kwargs['pk'])
        number = self.kwargs['number']
        season = models.TVShowSeason.objects.get(tvshow=tvshow,
                                                 number=number)
        return season


class TVShowSeasonCreateView(
    views.LoginRequiredMixin,
    generic.CreateView
):
    form_class = forms.TVShowSeasonForm
    model = models.TVShowSeason

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.tvshow = get_object_or_404(models.TVShow,
                                               pk=self.kwargs['pk'])
        self.object.save()
        actors_name = form.cleaned_data['actors_list'].split(', ')
        for name in actors_name:
            try:
                actor = models.Person.objects.get(name=name,
                                                  user=self.request.user)
            except ObjectDoesNotExist:
                actor = models.Person(name=name, user=self.request.user)
                actor.set_first_letter()
                actor.save()
            actor.tvshow_season_starred_in.add(self.object)
        return super(TVShowSeasonCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TVShowSeasonCreateView, self).get_context_data(
                **kwargs)
        tvshow = get_object_or_404(models.TVShow, pk=self.kwargs['pk'])
        context['tvshow'] = tvshow
        return context


class TVShowSeasonUpdateView(
    RestrictToUserMixin,
    generic.UpdateView
):
    form_class = forms.TVShowSeasonForm
    model = models.TVShowSeason

    def get_object(self):
        tvshow = get_object_or_404(models.TVShow, pk=self.kwargs['pk'])
        number = self.kwargs['number']
        season = models.TVShowSeason.objects.get(tvshow=tvshow,
                                                 number=number)
        return season

    def form_valid(self, form):
        self.object = form.save()

        # First we will delete this movie from all the
        # actors it's assotiatied with.
        # Then we will create new bonds.

        for actor in self.object.actors.all():
            actor.tvshow_season_starred_in.remove(self.object)

        actor_name = form.cleaned_data['actors_list'].split(', ')
        for name in actor_name:
            try:
                actor = models.Person.objects.get(name=name,
                                                  user=self.request.user)
            except ObjectDoesNotExist:
                actor = models.Person(name=name, user=self.request.user)
                actor.set_first_letter()
                actor.save()
            actor.tvshow_season_starred_in.add(self.object)
        return super(TVShowSeasonUpdateView, self).form_valid(form)


class TVShowSeasonDeleteView(
    RestrictToUserMixin,
    generic.DeleteView
):
    model = models.TVShowSeason
    # should change this url to 'movies:tvshow_detail' with pk
    success_url = reverse_lazy('movies:tvshow_list')

    def get_object(self):
        tvshow = get_object_or_404(models.TVShow, pk=self.kwargs['pk'])
        number = self.kwargs['number']
        season = models.TVShowSeason.objects.get(tvshow=tvshow,
                                                 number=number)
        return season


class PersonListView(
    RestrictToUserMixin,
    generic.ListView
):
    model = models.Person

    def get_queryset(self):
        queryset = super(PersonListView, self).get_queryset()
        letter = self.request.GET.get('letter', '')
        if letter:
            queryset = queryset.filter(user=self.request.user,
                                       first_letter=letter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)

        movies = models.Movie.objects.filter(user=self.request.user)
        letter = self.request.GET.get('letter', '')
        context['letter'] = letter

        movies = movies.all()
        movie_letters = []
        for letter in ascii_uppercase:
            for movie in movies:
                if (movie.first_letter == letter and
                        letter not in movie_letters):
                    movie_letters.append(letter)
                    break
        context['movie_letters'] = movie_letters

        persons = models.Person.objects.filter(user=self.request.user)
        russian_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
        person_letters = []
        for letter in russian_letters:
            for person in persons:
                if (person.first_letter == letter and
                        letter not in person_letters):
                    person_letters.append(letter)
                    break
        context['person_letters'] = person_letters

        return context


class PersonDetailView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.Person


class PersonDeleteView(
    RestrictToUserMixin,
    generic.DeleteView
):
    model = models.Person
    success_url = reverse_lazy('movies:person_list')


class GenreListView(
    generic.TemplateView
):
    template_name = 'movies/genre_list.html'

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        movies = models.Movie.objects.filter(user=self.request.user)
        genres = list(set([movie.genre for movie in movies]))
        genres.sort()
        context['genres'] = genres
        return context


class GenreDetailView(
    generic.TemplateView
):
    template_name = 'movies/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GenreDetailView, self).get_context_data(**kwargs)
        genre = self.request.GET.get('genre', '')
        if not genre:
            return redirect('movies:genre_list')
        movies = models.Movie.objects.filter(genre=genre,
                                             user=self.request.user)
        movies = movies.all()
        context['movies'] = movies
        context['genre'] = genre
        return context


class YearListView(
    generic.TemplateView
):
    template_name = 'movies/year_list.html'

    def get_context_data(self, **kwargs):
        context = super(YearListView, self).get_context_data(**kwargs)
        movies = models.Movie.objects.filter(user=self.request.user)
        years = list(set([movie.year for movie in movies]))
        years.sort()
        context['years'] = years
        return context


class YearDetailView(
    generic.TemplateView
):
    template_name = 'movies/year_detail.html'

    def get_context_data(self, **kwargs):
        context = super(YearDetailView, self).get_context_data(**kwargs)
        year = self.request.GET.get('year', '')
        if not year:
            return redirect('movies:year_list')
        movies = models.Movie.objects.filter(year=year,
                                             user=self.request.user)
        movies = movies.all()
        context['movies'] = movies
        context['year'] = year
        return context

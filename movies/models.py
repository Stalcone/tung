from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Person(models.Model):
    user = models.ForeignKey(User, related_name='persons')
    name = models.CharField(max_length=255)
    first_letter = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movies:person_detail', kwargs={'pk': self.pk})

    def set_first_letter(self):
        self.first_letter = self.name.split()[1][0]


class Movie(models.Model):
    user = models.ForeignKey(User, related_name='movies')
    name = models.CharField(max_length=255)
    first_letter = models.CharField(max_length=2, blank=True)
    image_url = models.URLField(blank=True)
    review_text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    grade = models.IntegerField()
    year = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    director_list = models.CharField(max_length=1000, blank=True)
    actors_list = models.CharField(max_length=3000, blank=True)
    director = models.ManyToManyField(Person, related_name='directed',
                                      blank=True)
    actors = models.ManyToManyField(Person, related_name='starred_in',
                                    blank=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.year)

    def get_absolute_url(self):
        return reverse('movies:movie_detail', kwargs={'pk': self.pk})

    def set_first_letter(self):
        if self.name[:3] == "The":
            self.first_letter = self.name[4]
        else:
            self.first_letter = self.name[0]


class TVShow(models.Model):
    user = models.ForeignKey(User, related_name='tvshows')
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)
    genre = models.CharField(max_length=255, blank=True)
    creator_list = models.CharField(max_length=1000, blank=True)
    creator = models.ManyToManyField(Person, related_name='created',
                                     blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movies:tvshow_detail', kwargs={'pk': self.pk})


class TVShowSeason(models.Model):
    user = models.ForeignKey(User, related_name='tvshow_seasons')
    tvshow = models.ForeignKey(TVShow, related_name='seasons')
    number = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)
    year = models.IntegerField()
    review_text = models.TextField()
    grade = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    actors_list = models.CharField(max_length=3000, blank=True)
    actors = models.ManyToManyField(Person,
                                    related_name='tvshow_season_starred_in')

    def __str__(self):
        return "{} — сезон {}".format(self.tvshow.name, self.number)

    def get_absolute_url(self):
        return reverse('movies:tvshow_season_detail',
                       kwargs={'pk': self.tvshow.pk, 'number': self.number})

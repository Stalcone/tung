from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ('name', 'year', 'genre', 'image_url', 'director_list',
                  'actors_list', 'review_text', 'grade')

    # director = forms.CharField()
    # actors = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'year',
            'image_url',
            'genre',
            'director_list',
            'actors_list',
            'review_text',
            'grade',
            ButtonHolder(Submit('create', 'Create', css_class='btn-primary'))
        )


class TVShowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields = ('name', 'genre', 'image_url', 'creator_list')

    def __init__(self, *args, **kwargs):
        super(TVShowForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'genre',
            'image_url',
            'creator_list',
            ButtonHolder(Submit('create', 'Create', css_class='btn-primary'))
        )


class TVShowSeasonForm(forms.ModelForm):
    class Meta:
        model = models.TVShowSeason
        fields = ('number', 'image_url', 'year', 'actors_list',
                  'review_text', 'grade')

    def __init__(self, *args, **kwargs):
        super(TVShowSeasonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'number',
            'image_url',
            'year',
            'actors_list',
            'review_text',
            'grade',
            ButtonHolder(Submit('create', 'Create', css_class='btn-primary'))
        )

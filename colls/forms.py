from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from . import models


class CollForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = models.Coll

    def __init__(self, *args, **kwargs):
        super(CollForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            ButtonHolder(Submit('create', 'Create', css_class='btn-primary'))
        )


class ItemForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'image_url', 'date', 'description')
        model = models.Item

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'image_url',
            'date',
            'description',
            ButtonHolder(Submit('add', 'Add', css_class='btn-primary'))
        )

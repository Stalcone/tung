from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Coll(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='colls')

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('colls:coll_detail', kwargs={'pk': self.pk})


class Item(models.Model):
    name = models.CharField(max_length=255)
    coll = models.ForeignKey(Coll, related_name='items')
    image_url = models.URLField(blank=True)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('colls:item_detail', kwargs={'pk': self.pk})

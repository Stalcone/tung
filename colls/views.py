from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic

from braces import views

from . import models, forms


class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CollListView(
    RestrictToUserMixin,
    generic.ListView
):
    model = models.Coll


class CollDetailView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.Coll

    def get_context_data(self, **kwargs):
        context = super(CollDetailView, self).get_context_data(**kwargs)
        self.obj = self.get_object()
        years = [item.date.year for item in self.obj.items.all()]
        years = sorted(list(set(years)), reverse=True)
        context['years'] = years
        return context


class CollYearView(
    RestrictToUserMixin,
    generic.DetailView
):
    model = models.Coll
    template_name = 'colls/coll_year.html'

    def get_context_data(self, **kwargs):
        context = super(CollYearView, self).get_context_data(**kwargs)
        year = self.kwargs['year']
        context['year'] = year

        months = range(1, 13)
        context['months'] = months

        self.obj = self.get_object()
        items = self.obj.items.all()
        # better change this line to .filter() but I don't know how
        items = [item for item in items if item.date.year == int(year)]

        months_items = {month: [] for month in months}

        for item in items:
            months_items[item.date.month].append(item)

        for month in months_items:
            items = []
            row = []
            for item in months_items[month]:
                row.append(item)
                if len(row) == 5:
                    items.append(row)
                    row = []
            if row:
                items.append(row)
            months_items[month] = items[:]

        context['months_items'] = months_items

        return context


class CollCreateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.CollForm
    headline = 'Create'
    model = models.Coll

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CollCreateView, self).form_valid(form)


class CollUpdateView(
    RestrictToUserMixin,
    views.SetHeadlineMixin,
    generic.UpdateView
):
    form_class = forms.CollForm
    headline = 'Edit'
    model = models.Coll


class CollDeleteView(
    RestrictToUserMixin,
    views.MessageMixin,
    generic.DeleteView
):
    model = models.Coll
    success_url = reverse_lazy('colls:index')

    def post(self, request, *args, **kwargs):
        self.messages.success("{} has been deleted".format(
            self.get_object().name))
        return super(CollDeleteView, self).post(request, *args, **kwargs)


class ItemDetailView(
    views.LoginRequiredMixin,
    generic.DetailView
):
    model = models.Item

    def get_queryset(self):
        return self.model.objects.filter(coll__user=self.request.user)


class ItemCreateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.ItemForm
    headline = 'Add'
    model = models.Item

    def get(self, request, *args, **kwargs):
        return super(ItemCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coll = get_object_or_404(models.Coll, pk=self.kwargs['pk'])
        self.object.save()
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.UpdateView
):
    form_class = forms.ItemForm
    headline = 'Edit'
    model = models.Item


class ItemDeleteView(
    views.LoginRequiredMixin,
    views.MessageMixin,
    generic.DeleteView
):
    model = models.Item

    def post(self, request, *args, **kwargs):
        self.messages.success("{} has been deleted".format(
            self.get_object().name))
        self.success_url = self.get_object().coll.get_absolute_url()
        return super(ItemDeleteView, self).post(request, *args, **kwargs)

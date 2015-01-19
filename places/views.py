from django.core.urlresolvers import reverse_lazy
from django.views import generic

from places.models import Place
from places.forms import NewPlaceForm

class IndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'place_list'
    model = Place


class PlaceDetailView(generic.DetailView):
    template_name = 'places/place_detail.html'
    model = Place

class NewPlaceCreateView(generic.CreateView):
    template_name = "places/create_new_place.html"
    success_url = reverse_lazy('places:creat_new_place')
    form_class = NewPlaceForm

    def form_valid(self, form):
        new_place = form.save()
        new_place.save()
        return super(NewPlaceCreateView, self).form_valid(form)
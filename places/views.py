from django.views import generic

from places.models import Place


class IndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'place_list'
    model = Place


class PlaceDetailView(generic.DetailView):
    template_name = 'places/place_detail.html'
    model = Place
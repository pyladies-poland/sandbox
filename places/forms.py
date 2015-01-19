from django import forms

from places.models import Place


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [
            'name',
            'description',
            'address_country',
            'address_city',
            'address_street',
            'address_post_code',
            ]
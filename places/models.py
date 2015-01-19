from django.db import models

from easy_maps.geocode import google_v3 as geocode

from django.utils.encoding import force_text

class Place(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=450)
    address_country = models.CharField(max_length=60)
    address_city = models.CharField(max_length=60)
    address_street = models.CharField(max_length=120)
    address_post_code = models.CharField(max_length=8)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    latitude = models.DecimalField(default=0, max_digits=16, blank=True,
                                   decimal_places=8)
    longitude = models.DecimalField(default=0, max_digits=16, blank=True,
                                    decimal_places=8)

    def __unicode__(self):
        return self.name

    def get_full_address(self):
        """
        create string with full address
        """
        return force_text(self.address_country) + \
               ", " + force_text(self.address_city) + \
               ", " + force_text(self.address_street)

    def fill_geocode(self):
        new_geocode = geocode(self.get_full_address())
        self.latitude = new_geocode[0]
        self.longitude = new_geocode[1]

    def save(self, *args, **kwargs):
        self.fill_geocode()
        super(Place, self).save(*args, **kwargs)


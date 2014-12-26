from django.db import models


class Place(models.Model):
    name = models.EmailField(max_length=100, unique=True)
    description = models.CharField(max_length=50)
    address_street = models.CharField(max_length=120)
    address_city = models.CharField(max_length=60)
    address_post_code = models.CharField(max_length=8)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.surname)

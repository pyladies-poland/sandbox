import datetime
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    GENDER = ((1, 'Female'), (2, 'Male'))

    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER)
    telephone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    register_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    activation_key = models.CharField(max_length=40, default='')
    akey_expires = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(2))
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.surname)

    @property
    def get_email(self):
        return self.email


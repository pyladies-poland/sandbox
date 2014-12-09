import datetime
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    GENDER = ((1, 'Female'), (2, 'Male'))

    user_email = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    user_gender = models.IntegerField(choices=GENDER)
    user_telephone_number = models.CharField(max_length=20)
    user_address = models.CharField(max_length=200)
    user_register_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user_register_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_activation_key = models.CharField(max_length=40, default='')
    user_akey_expires = models.DateTimeField(default=datetime.datetime.today() + datetime.timedelta(2))
    user_is_activ = models.BooleanField(default=False)

    def __unicode__(self):
        return '{} {}'.format(self.user_name, self.user_surname)

    @property
    def get_email(self):
        return self.user_email


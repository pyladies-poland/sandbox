from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_email = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    GENDER = ((1, 'Female'), (2, 'Male'))
    user_gender = models.IntegerField(choices=GENDER)
    user_telnr = models.CharField(max_length=20)
    user_addres = models.CharField(max_length=200)
    user_register_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user_register_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user_name +" "+ self.user_surname

    def get_email(self):
        return self.user_email
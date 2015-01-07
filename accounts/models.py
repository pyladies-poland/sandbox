import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class UserManager(BaseUserManager):


  def _create_user(self, email, password, active, staff, superuser,
                   **extra_fields):
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(email=email, staff=staff, active=active,
                      superuser=superuser, register_date=now, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email=None, password=None, **extra_fields):
    return self._create_user(email, password, False, False, False,
                 **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser):

    GENDER = ((1, 'Female'), (2, 'Male'))

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER, default=1)
    telephone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    register_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    activation_key = models.CharField(max_length=40, default='')
    date_of_birth = models.DateTimeField(default=timezone.now())
    akey_expires = models.DateTimeField(default=timezone.now() +
                                                datetime.timedelta(2))
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __unicode__(self):
        return '{} {}'.format(self.name, self.surname)

    @property
    def get_email(self):
        return self.email

    def get_short_name(self):
        return self.name

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.superuser

    def has_perm(self, perm, obj=None):
        return self.superuser

    def has_module_perms(self, app_label):
        return self.superuser

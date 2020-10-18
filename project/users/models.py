from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

ROLES =( 
    ("Admin", "Admin"), 
    ("Regular", "Regular"), 
) 
  

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Member(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False, default='')
    last_name = models.CharField(max_length=256, null=False, blank=False, default='')
    email = models.EmailField(max_length = 64, null =False, blank=False, default='', unique=True)
    phone = models.CharField(max_length = 64, null =False, blank=False, default='', unique=True)
    role =  models.CharField(choices=ROLES, default='Admin',max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", null=True)

    def __str__(self):
        return str(self.first_name)
from django.db import models
from testprj.helpers import random_int
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True)
    rand_field = models.IntegerField(default=random_int)

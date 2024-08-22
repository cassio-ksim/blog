from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Author(AbstractUser):
    groups = models.ManyToManyField(Group)
    user_permissions = models.ManyToManyField(Permission)
    class Meta:
        db_table = 'authors'
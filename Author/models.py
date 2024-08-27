from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User


class Author(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    groups = models.ManyToManyField(Group, related_name='author_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='author_permissions')
    class Meta:
        db_table = 'authors'
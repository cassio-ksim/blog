from django.db import models

class Author(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = 'authors'
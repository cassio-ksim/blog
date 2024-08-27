from django.db import models
from Author.models import Author


class Publication(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_publication = models.DateField(auto_now_add=True)
    pub_text = models.TextField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'publications'

from django.db import models

class Publication(models.Model):
    author = models.CharField(max_length=255)
    date_publication = models.DateField()
    pub_text = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
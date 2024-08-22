from django.db import models
from Author.models import Author

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publication = models.DateField()
    pub_text = models.TextField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'publications'

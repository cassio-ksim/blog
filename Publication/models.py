from django.db import models
from Author.models import Author
from django.contrib.auth.models import User

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publication = models.DateField()
    pub_text = models.TextField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'publications'


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='authors/profile_pictures', blank=True)
    

    def __str__(self):
        return self.user
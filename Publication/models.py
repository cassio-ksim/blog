from django.db import models

class Publication(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_publication = models.DateField(auto_now_add=True)
    pub_text = models.TextField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'publications'


class Comment(models.Model):
    post = models.ForeignKey(Publication, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

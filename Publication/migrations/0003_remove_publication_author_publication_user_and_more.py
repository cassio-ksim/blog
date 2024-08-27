# Generated by Django 4.2 on 2024-08-27 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Publication', '0002_author_alter_publication_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='author',
        ),
        migrations.AddField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
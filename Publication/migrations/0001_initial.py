# Generated by Django 5.0.7 on 2024-08-05 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_publication', models.DateField()),
                ('pub_text', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('author', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='Author.author')),
            ],
            options={
                'db_table': 'publications',
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_matrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Morbius',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('description', models.TextField(default=True, max_length=1000)),
                ('mob', models.FileField(upload_to='movie/%y')),
                ('thumb', models.FileField(blank=True, upload_to='thumb/%y')),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]

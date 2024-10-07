# Generated by Django 4.2.7 on 2024-10-07 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_remove_post_upvoted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='upvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

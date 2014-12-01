
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from taggit.managers import TaggableManager




class Scenario(models.Model):

    name = models.CharField(max_length=20, unique=True)
    order = models.IntegerField(max_length=3, default=0)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Library(models.Model):
    ref = models.CharField(max_length=10, unique=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(max_length=3, default=1, help_text="Duration in Minutes")
    location = models.CharField(max_length=30, blank=True, null=True)
    video = models.FileField(upload_to="uploads", help_text=".mp4 only")

    tags = TaggableManager()

    def __unicode__(self):
        return self.ref

    def get_absolute_url(self):
        return reverse('view', args=[self.id])


    class Meta:
        ordering = ['-added_on']
        get_latest_by = "added_on"
        verbose_name_plural = "Library"


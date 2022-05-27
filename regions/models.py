from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from generals import unicode_letters
from slugify import slugify

# Create your models here.
class CommonFields(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    slug = AutoSlugField(populate_from='title', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    
    

class Region(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    
    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

class RegionUnity(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_unities')

    class Meta:
        verbose_name = _("Region Unity")
        verbose_name_plural = _("Region Unities")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

class State(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    region_unity = models.ForeignKey(RegionUnity, on_delete=models.CASCADE, related_name='states')

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

class ZipCode(models.Model):
    number = models.PositiveSmallIntegerField()
    slug = models.SlugField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='zip_codes')

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.number))
        super().save(*args, **kwargs)
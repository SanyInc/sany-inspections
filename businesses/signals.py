from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Business, Store

@receiver(pre_save, sender=Business)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

@receiver(pre_save, sender=Store)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].notify_number)
    kwargs['instance'].slug = slug
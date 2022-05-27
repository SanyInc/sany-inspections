from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Customer, Inspector, BusinessOwner, HealthRegulator, Moderator, Admin

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    
    if created:
        if instance.role == 'Customer':
            Customer.objects.create(user=instance)
        elif instance.role == 'Inspector':
            Inspector.objects.create(user=instance)
        elif instance.role == 'Business Owner':
            BusinessOwner.objects.create(user=instance)
        elif instance.role == 'Health Regulator':
            HealthRegulator.objects.create(user=instance)
        elif instance.role == 'Moderator':
            Moderator.objects.create(user=instance)
        elif instance.role == 'Admin':
            Admin.objects.create(user=instance)
        Token.objects.create(user=instance)
        
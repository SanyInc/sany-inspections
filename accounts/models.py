from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from accounts.manager import UserManager
from regions.models import Region, RegionUnity, State, ZipCode

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    HEALTH_REGULATOR = 'Health Regulator'
    BUSINESS_OWNER = 'Business Owner'
    INSPECTOR = 'Inspector'
    CUSTOMER = 'Customer'
    ADMIN = 'Admin'
    MODERATOR = 'Moderator'
    
    DISPLAY_METHOD_CHOICES = [
        (HEALTH_REGULATOR, _("Health Regulator")),
        (BUSINESS_OWNER, _("Business Owner")),
        (INSPECTOR, _("Inspector")),
        (CUSTOMER, _("Customer")),
        (ADMIN, _("Admin")),
        (MODERATOR, _("Moderator")),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30 )
    last_name = models.CharField(_('last name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    role = models.CharField(_("role"), max_length=50, choices=DISPLAY_METHOD_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email


class Admin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class Moderator(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class BusinessOwner(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class Inspector(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    email_2 = models.EmailField(_('email address 2'), max_length=150, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="inspectors", blank=True, null=True)
    region_unity = models.ForeignKey(RegionUnity, on_delete=models.PROTECT, related_name="inspectors", blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="inspectors", blank=True, null=True)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.PROTECT, related_name="inspectors", blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address_number = models.PositiveSmallIntegerField(blank=True, null=True)
    partner = models.ForeignKey('Inspector', on_delete=models.PROTECT, related_name="inspector_partner", blank=True, null=True)
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

class HealthRegulator(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    store = models.OneToOneField('businesses.Store', on_delete=models.SET_NULL, blank=True, null=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True, related_name='health_regulator_creator')

    def __str__(self):
        return self.user.email
    
    def created_by(self):
        return self.user.created_by
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from regions.models import Region, RegionUnity, State, ZipCode
from checklists.models import Activity, TypeOfActivity
from generals import unicode_letters
from slugify import slugify


# from accounts.models import BusinessOwner
from regions.models import CommonFields

class Business(CommonFields):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    owner = models.ForeignKey('accounts.BusinessOwner', on_delete=models.SET_NULL, null=True)
    vat = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = _("Business")
        verbose_name_plural = _("Businessess")
        ordering = ("vat",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

    def owner_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.owner.user.first_name, self.owner.user.last_name)
        return full_name.strip()

class Store(models.Model):

    CENTRAL = 'Κεντρικό Κατάστημα'
    BRANCH = 'Υποκατάστημα'
    
    DISPLAY_METHOD_CHOICES = [
        (CENTRAL, _("Κεντρικό Κατάστημα")),
        (BRANCH, _("Υποκατάστημα")),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    business = models.ForeignKey(Business, on_delete=models.PROTECT, related_name="stores")
    category = models.CharField(_("Category"), max_length=50, choices=DISPLAY_METHOD_CHOICES)
    slug = models.SlugField(blank=True, null=True)
    # health_regulator = models.ForeignKey("accounts.HealthRegulator", on_delete=models.PROTECT)
    notify_number = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="stores")
    region_unity = models.ForeignKey(RegionUnity, on_delete=models.PROTECT, related_name="stores")
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="stores")
    zip_code = models.ForeignKey(ZipCode, on_delete=models.PROTECT, related_name="stores")
    address = models.CharField(max_length=100)
    address_number = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=150)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True, related_name="stores")
    type_of_activity = models.ForeignKey(TypeOfActivity, on_delete=models.SET_NULL, null=True, related_name="stores")

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")
        ordering = ("business__vat",)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.notify_number))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.notify_number)

    # def hr_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.HealthRegulator.user.first_name, self.healthregulator.user.last_name)
    #     return full_name.strip()
    
    def vat(self):
        return self.business.vat
    
    def owner(self):
        full_name = '%s %s' % (self.business.owner.user.first_name, self.business.owner.user.last_name)
        return full_name.strip()
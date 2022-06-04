from django.db import models
from django.utils.translation import gettext_lazy as _
from generals import unicode_letters
from slugify import slugify

class Activity(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(_("Display order"))

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)
        
class TypeOfActivity(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="type_of_activities")

    class Meta:
        verbose_name = _("Type of Activity")
        verbose_name_plural = _("Type of Activities")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="categories")
    order = models.PositiveSmallIntegerField(_("Display order"))

    class Meta:
        verbose_name = _("Tab")
        verbose_name_plural = _("Tabs")
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.activity})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

class Question(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_(
        "Category"), related_name="questions")
    choices = models.ManyToManyField('Choice')
    description = models.TextField(_("Description"))
    is_important = models.BooleanField(_("Is Important"), default=False)
    order = models.PositiveSmallIntegerField(_("Display order"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['order']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, replacements=unicode_letters)
        super().save(*args, **kwargs)

    def get_choices(self):
        return ", ".join([str(p) for p in self.choices.all()])

class Choice(models.Model):
    number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')

    def __str__(self):
        return str(self.number)

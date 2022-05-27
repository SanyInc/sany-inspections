import uuid
from django.conf import settings
from django.db import models
from businesses.models import Store
from checklists.models import Question
from django.utils.translation import gettext_lazy as _
from accounts.models import Inspector


class Inspection(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT, verbose_name=_(
        "Store"), related_name="inspections")
    inspector = models.ForeignKey(
        Inspector, verbose_name=_("Inspector"), null=True, on_delete=models.PROTECT)
    uuid = models.UUIDField(_("Inspection unique identifier"),
                            default=uuid.uuid4, primary_key=True, editable=False)
    date_created = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Inspection")
        verbose_name_plural = _("Inspections")
        ordering = ("-date_created",)

    def __str__(self):
        return str(self.uuid)


class Answer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_(
        "Checklist Item"), related_name="answers")
    body = models.PositiveSmallIntegerField(
        _("Choice"), blank=True, null=True)
    timestamp = models.DateTimeField(_("Timpestamp"), auto_now_add=True)
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT, verbose_name=_(
        "Inspection"), related_name="answers")
    comment = models.TextField(_("Comment"), blank=True, default="-")

    def __str__(self):
        return "{} to '{}' : '{}'".format(self.__class__.__name__, self.question, self.body)


class Complete(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    inspection = models.OneToOneField(Inspection, on_delete=models.PROTECT, verbose_name=_(
        "Inspection"))
    completed = models.DateTimeField(_("Complete date"), auto_now_add=True)
    score = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Completed")
        verbose_name_plural = _("Completed")
        ordering = ("-completed",)

    def __str__(self):
        return str(self.inspection)

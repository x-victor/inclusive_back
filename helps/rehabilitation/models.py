from django.db import models
from prose.fields import RichTextField

from core.models import BaseModel, ArchivedMixin, DateTimeMixin


class RehabilitationCenter(ArchivedMixin, DateTimeMixin, BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, default="")
    city = models.ForeignKey(
        "core.City",
        on_delete=models.PROTECT,
        related_name="rehabilitation_centers",
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=255, default="", blank=True)
    email = models.EmailField(default="", blank=True)
    description = RichTextField()
    website = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="rehabilitation_centers"
    )
    inclusions = models.ManyToManyField("core.InclusionTag")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Центр реабилитации"
        verbose_name_plural = "Центры реабилитации"
        ordering = ["name"]

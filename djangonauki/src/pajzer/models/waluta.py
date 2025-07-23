from enum import unique

from django.db import models


class Waluta(models.Model):
    code = models.CharField(
        max_length=5,
        unique=True,
        help_text="Trzy znaki z kodu ISO dla waluty (np PLN USD EUR)"
    )
    name = models.CharField(
        max_length=50
    )
    symbol = models.CharField(
        max_length=10,
        help_text="Symbol waluty np $"
    )
    numeric_code = models.PositiveSmallIntegerField(
        unique=True,
        null=True,
        blank=True,
        help_text="ISO 4217 kod waluty 840 USD"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Czy aktywna"
    )

    class Meta:
        verbose_name_plural = 'waluty'
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"

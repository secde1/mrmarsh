from django.db import models

from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Статус смен'
        verbose_name_plural = 'Статусы смены'


class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Статус Обед'
        verbose_name_plural = 'Статусы Обеда'

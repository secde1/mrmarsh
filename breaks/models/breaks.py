import pdb

from django.db import models
from django.contrib.auth import get_user_model

from breaks.constants import BREAK_CREATED_STATUS, BREAK_CREATED_DEFAULT
from breaks.models.dicts import BreakStatus
from breaks.models.replacements import Replacement

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(Replacement, on_delete=models.RESTRICT, related_name='breaks', verbose_name='Смена')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breaks',
                                 verbose_name='Сотрудник', blank=True)
    break_start = models.TimeField('Начало обеда', blank=True, null=True)
    break_end = models.TimeField('Конец обеда', blank=True, null=True)
    status = models.ForeignKey(BreakStatus, on_delete=models.RESTRICT, related_name='breaks', verbose_name='Статус',
                               blank=True)

    class Meta:
        verbose_name = 'Обеденней перерыв'
        verbose_name_plural = 'Обеденный перерывы'
        ordering = ('-replacement__date', 'break_start',)

    def __str__(self):
        return f'Обед пользователь {self.employee} ({self.pk})'

    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS ,
                defaults=BREAK_CREATED_DEFAULT
            )
            self.status = status
            # self.status = BreakStatus.objects.get(code=BREAK_TEST_STATUS)
        return super(Break, self).save(*args, **kwargs)

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Organisation(models.Model):
    name = models.CharField('Название', max_length=255)
    director = models.ForeignKey(
        User, related_name='organisations_directors', on_delete=models.RESTRICT, verbose_name='Директор'
    )
    employees = models.ManyToManyField(
        User, related_name='organisations_employees', verbose_name='Сотрудники',
        blank=True
    )

    class Meta:
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Group(models.Model):
    organisation = models.ForeignKey('breaks.Organisation', on_delete=models.CASCADE, related_name='groups',
                                     verbose_name='Организация')
    name = models.CharField('Название', max_length=255)
    manager = models.ForeignKey(
        User, models.RESTRICT, related_name='group_managers', verbose_name='Менеджер', blank=True,
    )
    employees = models.ManyToManyField(
        User, 'group_employees', verbose_name='Сотрудники', blank=True,
    )
    min_active = models.PositiveSmallIntegerField(
        'Минимально количество активных сотрудников', blank=True, null=True
    )
    break_start = models.TimeField('Начало обеда', blank=True, null=True)
    break_end = models.TimeField('Конец обеда', blank=True, null=True)
    break_max_duration = models.PositiveSmallIntegerField(
        'Максимальная длительность обеда', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'

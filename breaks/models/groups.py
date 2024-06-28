from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    organisation = models.ForeignKey('breaks.Organisation', on_delete=models.RESTRICT, related_name='groups',
                                     verbose_name='Организация')
    name = models.CharField('Название', max_length=255)
    manager = models.ForeignKey(
        User, models.RESTRICT, related_name='group_managers', verbose_name='Менеджер')
    employees = models.ManyToManyField(User, 'group_employees', verbose_name='Сотрудники', blank=True)
    min_active = models.PositiveSmallIntegerField('Минимально количество активных сотрудников', blank=True, null=True)
    break_start = models.TimeField('Начало обеда', blank=True, null=True)
    break_end = models.TimeField('Конец обеда', blank=True, null=True)
    break_max_duration = models.PositiveSmallIntegerField('Максимальная длительность обеда', blank=True, null=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'

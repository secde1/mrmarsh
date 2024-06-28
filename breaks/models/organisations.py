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
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'

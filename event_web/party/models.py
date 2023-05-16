from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=150, verbose_name='Імʼя')
    last_name = models.CharField(max_length=150, verbose_name='Прізвище')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('person', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'
        ordering = ['-created_at']

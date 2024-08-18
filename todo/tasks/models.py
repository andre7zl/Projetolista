from django.db import models
from django.core.exceptions import ValidationError

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError('A data de início não pode ser posterior à data de fim.')
        elif self.start_date is None or self.end_date is None:
            raise ValidationError('Ambas as datas de início e fim devem ser fornecidas.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

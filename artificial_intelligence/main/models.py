from django.db import models

class Predictions(models.Model):
    full_text = models.TextField('Текст для предсказаний')    
    def __str__(self) -> str:
        return str(self.id)
    class Meta:
        verbose_name = 'Предсказание'
        verbose_name_plural = 'Предсказания'

    
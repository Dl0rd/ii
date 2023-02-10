from .models import Predictions
from django.forms import ModelForm,Textarea


class PredictionsForm(ModelForm):
    class Meta:
        model = Predictions
        fields = ['full_text']
        widgets = {
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите текст для предсказания"
            })
        }
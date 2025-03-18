from django.forms import ModelForm
from .models import Logger  # Ensure this import is correct

class LogForm(ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
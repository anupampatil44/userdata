from django import forms
from .models import Data
# Create your models here.
CHOICES =(
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)
class Register(forms.ModelForm):
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)
    email = forms.EmailField()
    #gender=forms.MultipleChoiceField(CHOICES)
    class Meta:
        model=Data
        exclude=()
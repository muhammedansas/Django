from django.forms import ModelForm
from . models import Movies

class Fmovie(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        
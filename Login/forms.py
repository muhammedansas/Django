from django.forms import ModelForm
from . models import Dummyitems

class Dummy(ModelForm):
    class Meta:
        model = Dummyitems
        fields = '__all__'
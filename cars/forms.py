from django.forms import ModelForm
from .models import Cars



class CarModelForm(ModelForm):
    class Meta:
        model = Cars
        fields =  '__all__'
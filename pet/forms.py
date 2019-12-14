from django import forms
from pet.models import Pet

class PetForm(forms.ModelForm):
    """ Render and process a form based on the Pet model. """
    class Meta:
        model = Pet
        # fields = '__all__'
        exclude = ('owner',)

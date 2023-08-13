from django import forms

from charities.models import Charity


class CreateCharityForm(forms.ModelForm):
    class Meta:
        model = Charity
        fields = '__all__'
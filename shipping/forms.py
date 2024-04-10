from django import forms

from shipping.models import ShippingAddress
from util.validator import min_lenght_validator


class ShippingFrom(forms.ModelForm):
    state = forms.CharField(validators=[min_lenght_validator])

    class Meta:
        model = ShippingAddress
        fields = ['city', 'address', 'state', 'state']
        # exclude = ['created_at']

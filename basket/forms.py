from django import forms

from basket.models import Product


class BasketForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)
    quantity = forms.IntegerField()

    def save(self, basket):
        basket.add(self.cleaned_data['product'], self.cleaned_data.get('quantity'))
        return basket

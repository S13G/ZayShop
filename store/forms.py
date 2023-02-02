from django import forms

from store.models import Product


class DetailForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = ["sizes", "quantity"]
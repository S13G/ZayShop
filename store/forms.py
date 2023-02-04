from django import forms

from store.models import Product


class DetailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["sizes", "quantity"]

    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    EXTRA_LARGE = "XL"
    EXTRA_EXTRA_LARGE = "XXL"

    SIZE_CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
        (EXTRA_LARGE, "Xtra Large"),
        (EXTRA_EXTRA_LARGE, "Xtra-Xtra Large")
    )
    sizes = forms.ChoiceField(choices=SIZE_CHOICES, initial=SMALL)
    quantity = forms.IntegerField(min_value=1)

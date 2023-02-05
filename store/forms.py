from django import forms

from store.models import Product


class DetailForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = ["sizes", "quantity"]
        widgets = {
            "sizes": forms.Select
        }

    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args, **kwargs)

        self.fields['sizes'].widget.attrs.update(
            {'class': 'form-control form-select'})
        # self.fields['quantity'].widget.attrs.update({'class': 'badge bg-secondary'})

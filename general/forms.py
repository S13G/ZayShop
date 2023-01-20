from django import forms

from general.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control bg-dark border-light', 'placeholder': 'Email Address', 'id': 'subscribeEmail'})

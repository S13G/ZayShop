from django.contrib import messages
from django.shortcuts import render

from general.forms import NewsletterForm


# Create your views here.


def newsletter(request):
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.clean()
            newsletter_form.save()
            messages.success(request, "You have successfully signed up for the newsletter")
            # Creating new instance of the form
            newsletter_form = NewsletterForm()
        else:
            messages.info(request, "You have already signed up for the newsletter")
    else:
        newsletter_form = NewsletterForm()
    context = {"newsletter_form": newsletter_form}
    return render(request, "base.html", context)

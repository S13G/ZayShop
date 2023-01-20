from django.contrib import messages
from django.shortcuts import render

from general.forms import NewsletterForm, ContactForm


# Create your views here.


def home(request):
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
    return render(request, 'general/index.html')


def about(request):
    return render(request, 'general/about.html')


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.clean()
            contact_form.save()
            messages.success(request, "Form submitted successfully")
            # Creating new instance of the form
            contact_form = ContactForm()
        else:
            messages.info(request, "Error submitting form")
    else:
        contact_form = ContactForm()
    context = {"contact_form": contact_form}
    return render(request, 'general/contact.html', context)

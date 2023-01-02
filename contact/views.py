from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from .models import Contact, Address
from .forms import ContactForm


def contact(request):
    """
    User can send message through the form
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Confirmation email is sent on submission of form
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                topic,
                message,
                email_from,
                email_to
                )

            messages.success(request, 'Message submitted succesfully \
                A confirmation email is sent with original message')

    form = ContactForm
    company_address = Address.objects.all()

    context = {
        'form': form,
        'company_address': company_address,
    }

    template = 'contact/contact.html'

    return render(request, template, context)

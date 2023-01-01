from django.shortcuts import render
from django.contrib import messages
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
            messages.success(request, 'Messae submitted succesfully')

    form = ContactForm
    compnay_address = Address.objects.all()

    context = {
        'form': form,
        'compnay_address': compnay_address,
    }

    template = 'contact/contact.html'

    return render(request, template, context)

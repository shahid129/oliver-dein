from django.shortcuts import render
from .models import Faqs


def faqs(request):
    faqs = Faqs.objects.all()

    template = 'faqs/faqs.html'

    context = {
        'faqs': faqs,
    }

    return render(request, template, context)
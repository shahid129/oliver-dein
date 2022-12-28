from django.http import HttpResponse


class StripeWH_Handler:
    """ Handles stripe webshooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic, unknown, unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'payment failed Webhook received: {event["type"]}',
            status=200
        )

from django.shortcuts import render
from rest_framework import viewsets
from .models import RegisterUser, Product
from .serializers import RegisterUserSerializer
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json



stripe.api_key = settings.STRIPE_PRIVATE_KEY


# Create your views here.

class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = RegisterUser.objects.all()
    serializer_class = RegisterUserSerializer



class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        products_id = self.kwargs['pk']
        product = Product.objects.get(id=products_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price_data': {
                        'currency': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                        },
                        'quantity': 1,
                    },
                    ],
                    metadata={
                        'product_id': product.id,
                    },

                mode='payment',
                success_url=YOUR_DOMAIN + '/success',
                cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({
            'id': checkout_session.id
        })




class ProductLandingPage(TemplateView):
    template_name = 'landing.html'


    def get_context_data(self, **kwargs):

        product = Product.objects.get(name="Test Product")
        context = super(ProductLandingPage, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context



class SuccessView(TemplateView):
    template_name = 'success.html'
class CancelView(TemplateView):
    template_name = 'cancel.html'




@csrf_exempt
def stripe_webhook(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)
  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
    session = event['data']['object']['id'],

    customer_email = session['customer_details']['email']
    product_id = session['metadata']['product_id']


    product = Product.objects.get(id=product_id)

    send_mail(
        subject="Here is your product",
        message="Thanks for your purchase. Here is the product that you ordered.",
        recipient_list=[customer_email],
        from_email='eliud@eliud.com'
    )

  elif event['type'] == 'payment_intent.succeeded':
    intent = event ['data']['object']

    stripe_customer_id = intent['customer']
    stripe_customer =stripe.Customer.retrieve(stripe_customer_id)

    customer_email = stripe_customer['email']
    product_id = session['metadata']['product_id']

    product = Product.objects.get(id=product_id)

    send_mail(
        subject="Here is your product",
        message="Thanks for your purchase. Here is the product that you ordered.",
        recipient_list=[customer_email],
        from_email='eliud@eliud.com'
    )

  return HttpResponse(status=200)





class StripeIntentView(View):
    def post(self, request, *args, **kwargs ):
        try:
            req_json =json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            products_id = self.kwargs['pk']
            product = Product.objects.get(id=products_id)
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata ={
               "product_id": product.id
                },
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({"error":str(e)}), 403
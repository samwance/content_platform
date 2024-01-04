import stripe
from django.conf import settings
from django.views.generic import FormView
from .forms import SubscriptionForm
from .models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY


class SubscriptionView(FormView):
    template_name = "subscription/subscribe.html"
    form_class = SubscriptionForm
    success_url = "/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        card_number = form.cleaned_data["card_number"]
        exp_month = form.cleaned_data["exp_month"]
        exp_year = form.cleaned_data["exp_year"]
        cvc = form.cleaned_data["cvc"]

        # Create a customer object in Stripe
        customer = stripe.Customer.create(
            name=name,
            email=email,
            source={
                "object": "card",
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )

        # Create a subscription for the customer
        stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": 100}],
            payment_behavior="default_incomplete",
            expand=["latest_invoice.payment_intent"],
        )

        # Create and save the Subscription object
        Subscription.objects.create(user=self.request.user, is_active=True)

        # Redirect to success page
        return super().form_valid(form)

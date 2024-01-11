from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class SubscriptionView(TemplateView):
    """Страница приобретения подписки"""

    template_name = "subscription/subscribe.html"


class SuccessView(TemplateView):
    """Успешная оплата"""
    template_name = "subscription/success.html"

    def get(self, request, *args, **kwargs):
        # Retrieve the authenticated user
        user = self.request.user
        # Update the user's is_subscribed field upon successful payment
        user.is_subscribed = True
        user.save()
        # Render the success template
        return render(request, self.template_name, {'user': user})


class CancelView(TemplateView):
    """Оплата не произведена"""

    template_name = "subscription/cancel.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        # Создаем подписку как объект платежа Stripe

        product = stripe.Product.create(
            # Данные для отображения на странице оплаты
            name="Бессрочная подписка",
            default_price_data={
                "unit_amount": 10000,
                "currency": "rub",
            },
            expand=["default_price"],
        )

        # Формируем цену подписки

        my_price = stripe.Price.create(
            product=product["id"],
            unit_amount=10000,
            currency="rub",
        )

        # Создаем сессию оплаты подписки

        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": my_price["id"],
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/",
        )

        return redirect(session.url, code=303)
# from .forms import SubscriptionForm
# from .models import Subscription
#
# stripe.api_key = settings.STRIPE_SECRET_KEY
#
#
# class SubscriptionView(FormView):
#     template_name = "subscription/subscribe.html"
#     form_class = SubscriptionForm
#     success_url = "/"
#
#     def form_valid(self, form):
#         name = form.cleaned_data["name"]
#         email = form.cleaned_data["email"]
#         card_number = form.cleaned_data["card_number"]
#         exp_month = form.cleaned_data["exp_month"]
#         exp_year = form.cleaned_data["exp_year"]
#         cvc = form.cleaned_data["cvc"]
#
#         # Create a customer object in Stripe
#         customer = stripe.Customer.create(
#             name=name,
#             email=email,
#             source={
#                 "object": "card",
#                 "number": card_number,
#                 "exp_month": exp_month,
#                 "exp_year": exp_year,
#                 "cvc": cvc,
#             },
#         )
#
#         # Create a subscription for the customer
#         stripe.Subscription.create(
#             customer=customer.id,
#             items=[{"price": 100}],
#             payment_behavior="default_incomplete",
#             expand=["latest_invoice.payment_intent"],
#         )
#
#         # Create and save the Subscription object
#         Subscription.objects.create(user=self.request.user, is_active=True)
#
#         # Redirect to success page
#         return super().form_valid(form)

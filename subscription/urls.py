from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionView, SuccessView, CancelView, CreateCheckoutSessionView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('buy/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

]

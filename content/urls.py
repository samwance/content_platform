from django.urls import path

from content.apps import ContentConfig
from content.views import IndexView, ContentCreate

app_name = ContentConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', ContentCreate.as_view(), name='content_create'),
    # path('content/<pk>/', ContentRetrieve.as_view(), name='content_create'),
]
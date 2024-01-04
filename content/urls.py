from django.urls import path

from content.apps import ContentConfig
from content.views import (
    IndexView,
    ContentCreate,
    PaidContentList,
    ContentDetail,
    ContentUpdate,
    ContentDelete,
)

app_name = ContentConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", ContentCreate.as_view(), name="content_create"),
    path("post/<pk>/", ContentDetail.as_view(), name="content_detail"),
    path("post/<pk>/update/", ContentUpdate.as_view(), name="content_update"),
    path("post/<pk>/delete/", ContentDelete.as_view(), name="content_delete"),
    path("paid/", PaidContentList.as_view(), name="paid_content"),
]

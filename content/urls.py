from django.urls import path

from content.apps import ContentConfig
from content.views import (
    IndexView,
    ContentCreate,
    PaidContentList,
    ContentDetail,
    ContentUpdate,
    ContentDelete,
    CollectionCreate,
    CollectionDetail,
    CollectionUpdate,
    CollectionDelete,
    CollectionList,
)

app_name = ContentConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/create/", ContentCreate.as_view(), name="content_create"),
    path("post/<pk>/", ContentDetail.as_view(), name="content_detail"),
    path("post/<pk>/update/", ContentUpdate.as_view(), name="content_update"),
    path("post/<pk>/delete/", ContentDelete.as_view(), name="content_delete"),
    path("paid/", PaidContentList.as_view(), name="paid_content"),
    path("cols/", CollectionList.as_view(), name="collection_list"),
    path("col/create/", CollectionCreate.as_view(), name="collection_create"),
    path("col/<pk>/", CollectionDetail.as_view(), name="collection_detail"),
    path("col/<pk>/edit/", CollectionUpdate.as_view(), name="collection_update"),
    path("col/<pk>/delete/", CollectionDelete.as_view(), name="collection_delete"),
]

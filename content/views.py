from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.html import linebreaks
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from subscription.models import Subscription
from .forms import ContentForm, CollectionForm
from .models import Content, Collection


class IndexView(TemplateView):
    template_name = "content/index.html"
    extra_context = {"title": "Главная страница"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["object_list"] = Content.objects.filter(is_free=True)
        return context_data


class ContentCreate(LoginRequiredMixin, CreateView):
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy("content:index")

    def form_valid(self, form):
        # При создании поста - объект автоматически привязывается к пользователю

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PaidContentList(ListView):
    model = Content
    template_name = "content/paid_content_list.html"
    fields = "__all__"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if Subscription.objects.filter(user=self.request.user).exists():
                return Content.objects.all()
            else:
                return None
        else:
            return None

    def get_context_data(self, **kwargs):
        """Формируем данные для отображения в шаблоне страницы платного контента"""

        context_data = super().get_context_data(**kwargs)

        return context_data


class ContentDetail(DetailView):
    model = Content
    template_name = "content/content_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        content_item = Content.objects.get(pk=self.kwargs.get("pk"))
        context_data["title"] = content_item.name
        return context_data


class ContentUpdate(LoginRequiredMixin, UpdateView):
    model = Content
    form_class = ContentForm
    template_name = 'content/content_update.html'
    success_url = reverse_lazy("content:content_detail")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        content_item = Content.objects.get(pk=self.kwargs.get("pk"))
        context_data["title"] = content_item.name
        return context_data

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to edit this content")
        return obj


class ContentDelete(DeleteView):
    model = Content
    success_url = reverse_lazy("content:index")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to delete this content")
        return obj


class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    success_url = reverse_lazy("content:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CollectionDelete(DeleteView):
    model = Collection
    success_url = reverse_lazy("content:index")
    template_name = 'content/collection_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to delete this collection")
        return obj


class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    success_url = reverse_lazy("content:collection_detail")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        content_item = Collection.objects.get(pk=self.kwargs.get("pk"))
        context_data["title"] = content_item.name
        return context_data

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to edit this collection")
        return obj


class CollectionDetail(DetailView):
    model = Collection

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        collection_item = Collection.objects.get(pk=self.kwargs.get("pk"))
        collection = self.object
        context_data["title"] = collection_item.name
        context_data["posts"] = Content.objects.filter(collection=collection)
        return context_data

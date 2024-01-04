import datetime

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import ContentForm
from .models import Album, Content


class IndexView(TemplateView):
    template_name = 'content/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Content.objects.all()
        return context_data


class AlbumList(CreateView):
    model = Album
    template_name = 'content/album_list.html'
    fields = '__all__'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'content/album_detail.html'


class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'content/album_form.html'
    fields = '__all__'


class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'


class ContentCreate(CreateView):
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy("content:index")

    def form_valid(self, form):
        # При создании поста - объект автоматически привязывается к пользователю

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ContentList(CreateView):
    model = Content
    template_name = 'content/content_list.html'
    fields = '__all__'


class ContentDetail(DetailView):
    model = Content
    template_name = 'content/content_detail.html'


class ContentUpdate(UpdateView):
    model = Content
    template_name = 'content/content_form.html'
    fields = '__all__'


class ContentDelete(DeleteView):
    model = Content
    success_url = '/contents/'

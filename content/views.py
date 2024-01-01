from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Album, Content


class IndexView(TemplateView):
    template_name = 'content/index.html'
    extra_context = {
        'title': 'Главная страница'
    }


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

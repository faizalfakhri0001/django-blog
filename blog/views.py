from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
)
# Create your views here.
from .models import Artikel
from .forms import AddForm, EditForm


class BlogUpdate(UpdateView):
    model = Artikel
    form_class = EditForm
    template_name = "blog/blog_update.html"


class BlogDelete(DeleteView):
    model = Artikel
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy('blog:manage')


class BlogManage(ListView):
    model = Artikel
    template_name = "blog/blog_manage.html"
    context_object_name = 'artikels'


class BlogCreate(CreateView):
    form_class = AddForm
    template_name = "blog/blog_create.html"


class BlogCategory(ListView):
    model = Artikel
    template_name = "blog/blog_kategori.html"
    context_object_name = 'artikels'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list(
            'kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class BlogDetail(DetailView):
    model = Artikel
    template_name = "blog/blog_detail.html"
    context_object_name = 'artikels'


class BlogList(ListView):
    model = Artikel
    template_name = "blog/blog_list.html"
    context_object_name = 'artikels'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list(
            'kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class LastUpdateArtikel():
    model = Artikel

    def latest_artikel(self):
        last_artikel = self.model.objects.values_list(
            'kategori', flat=True).distinct()
        queryset = []

        for artikels in last_artikel:
            artikel = self.model.objects.filter(
                kategori=artikels).latest('published')
            queryset.append(artikel)

        return queryset

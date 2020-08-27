from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import(
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Artikel, Category
from .forms import AddForm, EditForm


class BlogSearch(ListView):
    def get(self, request, *args, **kwargs):
        queryset = Artikel.objects.all()
        query = request.GET.get('q')
        # print(query)
        if query:
            queryset = queryset.filter(Q(judul__icontains=query)).distinct()

        context = {
            'artikels': queryset,
        }
        return render(request, 'blog/blog_search.html', context)


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Artikel
    form_class = EditForm
    template_name = "blog/blog_update.html"


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Artikel
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy('blog:manage')


class BlogManage(LoginRequiredMixin, ListView):
    model = Artikel
    template_name = "blog/blog_manage.html"
    context_object_name = 'artikels'

    def get_context_data(self, *args, **kwargs):
        artikel = self.model.objects.filter(author=self.request.user)
        self.kwargs.update({'artikels': artikel})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class BlogCreate(LoginRequiredMixin, CreateView):
    form_class = AddForm
    template_name = "blog/blog_create.html"


class BlogCategory(ListView):
    model = Artikel
    # category = Category
    template_name = "blog/blog_kategori.html"
    context_object_name = 'artikels'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            kategori__slug=self.kwargs['slug'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.order_by(
            'kategori').distinct('kategori').values_list(
                'kategori__slug', flat=True).exclude(
                    kategori__slug=self.kwargs['slug'])

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
            'kategori__slug', flat=True).distinct()

        # print(set(kategori_list))
        self.kwargs.update({'kategori_list': set(kategori_list)})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class LastUpdateArtikel():
    model = Artikel

    def latest_artikel(self):
        last_artikel = self.model.objects.values_list(
            'kategori__name', flat=True).order_by('kategori__name').distinct('kategori__name')

        queryset = []
        for artikels in last_artikel:
            artikel = self.model.objects.filter(
                kategori__name=artikels).latest('published')
            queryset.append(artikel)

        return queryset

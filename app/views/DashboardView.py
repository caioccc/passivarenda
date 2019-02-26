from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import ContextMixin

from app.models import Post, Categoria, Tag, Email


class CustomContextHomeMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('?')
        if posts.count() > 3:
            kwargs['latest'] = posts[:3]
        else:
            kwargs['latest'] = posts
        return super(CustomContextHomeMixin, self).get_context_data(**kwargs)


class CustomContextBlogMixin(CustomContextHomeMixin):
    def get_context_data(self, **kwargs):
        kwargs['categorias'] = Categoria.objects.all()
        kwargs['tags'] = Tag.objects.all()
        return super(CustomContextBlogMixin, self).get_context_data(**kwargs)


class HomeView(TemplateView, CustomContextHomeMixin):
    template_name = 'blog/index.html'


class ContactView(HomeView):
    template_name = 'blog/contact.html'


class ViewPost(DetailView, CustomContextBlogMixin):
    model = Post
    template_name = 'blog/post.html'
    pk_url_kwarg = 'post_id'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class ViewCapturaPlanilha(CreateView, CustomContextBlogMixin):
    model = Email
    context_object_name = 'email'
    fields = ['email']
    template_name = 'blog/captura_planilha.html'

    def get_success_url(self):
        return reverse('post_download', kwargs={'post_id': self.kwargs['post_id']})

    def get_context_data(self, **kwargs):
        kwargs['post'] = Post.objects.get(pk=self.kwargs['post_id'])
        return super(ViewCapturaPlanilha, self).get_context_data(**kwargs)

    def form_valid(self, form):
        return super(ViewCapturaPlanilha, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViewCapturaPlanilha, self).form_invalid(form)


class ViewPostDownload(DetailView, CustomContextBlogMixin):
    model = Post
    template_name = 'blog/post_download.html'
    pk_url_kwarg = 'post_id'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class CategoriaView(ListView, CustomContextBlogMixin):
    template_name = 'blog/blog.html'
    model = Post
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs.get('categoria_id')).order_by('?')


class BlogView(CategoriaView):
    ordering = '-created_at'

    def get_queryset(self):
        return Post.objects.all()


class InfograficoView(CategoriaView):
    def get_queryset(self):
        return Post.objects.filter(categoria__categoria__icontains='nfografic').order_by('?')


class VideoView(CategoriaView):
    def get_queryset(self):
        return Post.objects.filter(categoria__categoria__icontains='video')


class SlideView(CategoriaView):
    def get_queryset(self):
        return Post.objects.filter(categoria__categoria__icontains='slide')


class CitacaoView(CategoriaView):
    def get_queryset(self):
        return Post.objects.filter(categoria__categoria__icontains='citac')

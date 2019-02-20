from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import ContextMixin

from app.models import Post, Categoria, Tag


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


# class InfograficoView(ListView):
#     template_name = 'blog/blog.html'
#     model = Post
#     paginate_by = 6
#     context_object_name = 'posts'
#
#     def get_queryset(self):
#         return Post.objects.filter(categoria__categoria__contains='Info').order_by('?')
#
#     def get_context_data(self, **kwargs):
#         latest = Post.objects.all().order_by('?')
#         kwargs['categorias'] = Categoria.objects.all()
#         kwargs['tags'] = Tag.objects.all()
#         if latest.count() > 3:
#             kwargs['latest'] = latest[:3]
#         else:
#             kwargs['latest'] = latest
#         return super(InfograficoView, self).get_context_data(**kwargs)

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

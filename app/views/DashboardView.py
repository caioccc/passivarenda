from django.views.generic import TemplateView, ListView, DetailView

from app.models import Post, Categoria, Tag


class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('?')
        if posts.count() > 3:
            kwargs['latest'] = posts[3]
        else:
            kwargs['latest'] = posts
        return super(HomeView, self).get_context_data(**kwargs)


class ViewPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    pk_url_kwarg = 'post_id'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        latest = Post.objects.all().order_by('?')
        kwargs['categorias'] = Categoria.objects.all()
        kwargs['tags'] = Tag.objects.all()
        if latest.count() > 3:
            kwargs['latest'] = latest[3]
        else:
            kwargs['latest'] = latest
        return super(ViewPost, self).get_context_data(**kwargs)


class CategoriaView(ListView):
    template_name = 'blog/blog.html'
    model = Post
    paginate_by = 7
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs.get('categoria_id')).order_by('?')

    def get_context_data(self, **kwargs):
        latest = Post.objects.all().order_by('?')
        kwargs['categorias'] = Categoria.objects.all()
        kwargs['tags'] = Tag.objects.all()
        if latest.count() > 3:
            kwargs['latest'] = latest[3]
        else:
            kwargs['latest'] = latest
        return super(CategoriaView, self).get_context_data(**kwargs)


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = Post
    context_object_name = 'posts'
    ordering = '-created_at'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        latest = Post.objects.all().order_by('?')
        kwargs['categorias'] = Categoria.objects.all()
        kwargs['tags'] = Tag.objects.all()
        if latest.count() > 3:
            kwargs['latest'] = latest[3]
        else:
            kwargs['latest'] = latest
        return super(BlogView, self).get_context_data(**kwargs)


class ContactView(TemplateView):
    template_name = 'blog/contact.html'
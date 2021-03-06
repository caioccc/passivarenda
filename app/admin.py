from django.contrib import admin

from app.models import Categoria, Tag, Post, Email

"""
admin.py: Definicao de classes para gerenciar no painel de admin do Django.
"""
__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


class PostAdmin(admin.ModelAdmin):
    search_fields = (
        'created_at', 'titulo'
    )
    list_display = ('id', 'categoria', 'titulo', 'slug', 'resumo', 'autor', 'views', 'comments')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Email, EmailAdmin)

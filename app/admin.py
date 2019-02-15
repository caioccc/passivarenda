from django.contrib import admin

# from app.models import *

"""
admin.py: Definicao de classes para gerenciar no painel de admin do Django.
"""
__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


# class ItemVendaInline(admin.TabularInline):
#     model = ItemVenda


# class VendaInline(admin.TabularInline):
#     model = Venda


# class ClienteAdmin(admin.ModelAdmin):
#     search_fields = (
#         'telefone',
#     )
#     inlines = [VendaInline, ]
#     list_display = (
#         'id', 'nome', 'qtd_pedidos', 'telefone', 'facebook_url', 'instagram_url', 'email', 'created_at')

#     def qtd_pedidos(self, obj):
#         return int(obj.venda_set.all().count())

#     def nome_cliente(self, obj):
#         return obj.usuario.first_name


# class EntradaAdmin(admin.ModelAdmin):
#     search_fields = (
#         'created_at',
#     )
#     list_display = (
#         'id', 'ref', 'desc', 'valor', 'created_at')


# class SaidaAdmin(admin.ModelAdmin):
#     search_fields = (
#         'created_at',
#     )
#     list_display = (
#         'id', 'ref', 'desc', 'valor', 'created_at')


# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'categoria', 'created_at')


# class TagPromoAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'tag', 'created_at')


# class FonteAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'fonte', 'created_at')


# class StatusAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'status', 'created_at')


# class TamanhoAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'tamanho', 'created_at')


# class ProdutoAdmin(admin.ModelAdmin):
#     search_fields = (
#         'nome',
#     )
#     list_filter = ('tag_promo__tag', 'categoria__categoria',)
#     list_display = (
#         'id', 'cod_ref', 'nome', 'cor', 'url_foto', 'tag_promo', 'categoria', 'valor_compra', 'valor_venda',
#         'lucro_aproximado', 'qtd', 'created_at')


# class VendaAdmin(admin.ModelAdmin):
#     search_fields = (
#         'cliente',
#     )
#     inlines = [ItemVendaInline, ]
#     list_filter = ('cliente__nome', 'fonte__fonte', 'status__status')
#     list_display = (
#         'id', 'cliente', 'desconto', 'valor_total', 'status', 'fonte', 'created_at')


# class ItemVendaAdmin(admin.ModelAdmin):
#     search_fields = (
#         'produto',
#     )
#     list_display = (
#         'id', 'venda', 'produto', 'valor_total_item', 'desconto', 'qtd', 'created_at')


# admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Entrada, EntradaAdmin)
# admin.site.register(Saida, SaidaAdmin)
# admin.site.register(Categoria, CategoriaAdmin)
# admin.site.register(TagPromo, TagPromoAdmin)
# admin.site.register(Fonte, FonteAdmin)
# admin.site.register(Status, StatusAdmin)
# admin.site.register(Produto, ProdutoAdmin)
# admin.site.register(Venda, VendaAdmin)
# admin.site.register(ItemVenda, ItemVendaAdmin)
# admin.site.register(Cor)
# admin.site.register(Tamanho)
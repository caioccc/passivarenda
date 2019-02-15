# coding=utf-8
from __future__ import unicode_literals

from base64 import b64encode

import pyimgur
from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


# class BaseAddress(models.Model):
#     class Meta:
#         abstract = True

#     endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='Endereço')
#     numero = models.CharField(max_length=5, blank=True, null=True, verbose_name='Número')
#     bairro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Bairro')
#     complemento = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ponto de Referência')


# class Cliente(BaseAddress, TimeStamped):
#     nome = models.CharField(max_length=300, blank=True, null=True, verbose_name='Nome')
#     telefone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Telefone')
#     facebook_url = models.URLField(blank=True, null=True)
#     instagram_url = models.URLField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)

#     def __str__(self):
#         return u'%s' % (self.nome)

#     def __unicode__(self):
#         return u'%s' % (self.nome)


# class Entrada(TimeStamped):
#     ref = models.CharField(max_length=300, blank=True, null=True, verbose_name='Referência')
#     desc = models.CharField(max_length=300, blank=True, null=True, verbose_name='Descrição')
#     valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', verbose_name='Valor')

#     def __str__(self):
#         return u'%s' % (self.ref)

#     def __unicode__(self):
#         return u'%s' % (self.ref)


# class Saida(TimeStamped):
#     class Meta:
#         verbose_name = u'Saída'
#         verbose_name_plural = u'Saídas'

#     ref = models.CharField(max_length=300, blank=True, null=True, verbose_name='Referência')
#     desc = models.CharField(max_length=300, blank=True, null=True, verbose_name='Descrição')
#     valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL', verbose_name='Valor')

#     def __str__(self):
#         return u'%s' % (self.ref)

#     def __unicode__(self):
#         return u'%s' % (self.ref)


# class Categoria(TimeStamped):
#     categoria = models.CharField(max_length=300, blank=True, null=True, verbose_name='Categoria')

#     def __str__(self):
#         return u'%s' % (self.categoria)

#     def __unicode__(self):
#         return u'%s' % (self.categoria)


# class TagPromo(TimeStamped):
#     tag = models.CharField(max_length=300, blank=True, null=True, verbose_name='Tag')

#     def __str__(self):
#         return u'%s' % (self.tag)

#     def __unicode__(self):
#         return u'%s' % (self.tag)


# class Fonte(TimeStamped):
#     fonte = models.CharField(max_length=300, blank=True, null=True, verbose_name='Fonte')

#     def __str__(self):
#         return u'%s' % (self.fonte)

#     def __unicode__(self):
#         return u'%s' % (self.fonte)


# class Cor(TimeStamped):
#     class Meta:
#         verbose_name = u'Cor'
#         verbose_name_plural = u'Cores'

#     cor = models.CharField(max_length=300, blank=True, null=True, verbose_name='Cor')

#     def __str__(self):
#         return u'%s' % (self.cor)

#     def __unicode__(self):
#         return u'%s' % (self.cor)


# class Tamanho(TimeStamped):
#     tamanho = models.CharField(max_length=300, blank=True, null=True, verbose_name='Tamanho')

#     def __str__(self):
#         return u'%s' % (self.tamanho)

#     def __unicode__(self):
#         return u'%s' % (self.tamanho)


# class Produto(TimeStamped):
#     cod_ref = models.CharField(max_length=300, blank=True, null=True, verbose_name='Código')
#     cor = models.ForeignKey(Cor, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Cor')
#     nome = models.CharField(max_length=300, blank=True, null=True, verbose_name='Nome')
#     foto = models.FileField(blank=True, null=True, default='http://placehold.it/100x100')
#     url_foto = models.URLField(blank=True, null=True, default='http://placehold.it/100x100',
#                                verbose_name='Link da Foto')
#     tag_promo = models.ForeignKey(TagPromo, on_delete=models.CASCADE)
#     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#     valor_compra = MoneyField(max_digits=14, blank=True, null=True, decimal_places=2, default_currency='BRL',
#                               verbose_name='Valor de Compra')
#     valor_venda = MoneyField(max_digits=14, blank=True, null=True, decimal_places=2, default_currency='BRL',
#                              verbose_name='Valor de Venda')
#     lucro_aproximado = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL',
#                                   verbose_name='Lucro Aproximado')
#     qtd = models.IntegerField(verbose_name='Quantidade', default=1)
#     tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return u'%s - %s - %s' % (self.nome, self.tamanho, self.cor)

#     def __unicode__(self):
#         return u'%s - %s - %s' % (self.nome, self.tamanho, self.cor)

#     def save(self, *args, **kwargs):
#         if self.valor_compra and self.valor_venda:
#             subtotal = float(str(self.valor_venda.amount).replace(',', '.')) - float(
#                 str(self.valor_compra.amount).replace(',', '.'))
#             subtotal = float(format(subtotal, '.2f'))
#             self.lucro_aproximado = Money(subtotal, 'BRL')
#         if not self.url_foto:
#             try:
#                 CLIENT_ID = "cdadf801dc167ab"
#                 bencode = b64encode(self.foto.read())
#                 client = pyimgur.Imgur(CLIENT_ID)
#                 r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
#                 file = r['link']
#                 self.url_foto = file
#             except (Exception,):
#                 pass
#         return super(Produto, self).save(*args, **kwargs)


# class Status(TimeStamped):
#     class Meta:
#         verbose_name = u'Status'
#         verbose_name_plural = u'Status'

#     status = models.CharField(max_length=300, blank=True, null=True, verbose_name='Status')

#     def __str__(self):
#         return u'%s' % (self.status)

#     def __unicode__(self):
#         return u'%s' % (self.status)


# class Venda(TimeStamped):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     desconto = models.CharField(max_length=5, blank=True, null=True, verbose_name='Desconto', default='0')
#     valor_total = MoneyField(max_digits=14, blank=True, null=True, decimal_places=2, default_currency='BRL',
#                              verbose_name='Valor Total')
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)
#     fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE)

#     def __str__(self):
#         return u'%s' % (self.pk)

#     def __unicode__(self):
#         return u'%s' % (self.pk)

#     def save(self, *args, **kwargs):
#         if self.itemvenda_set.all().count() > 0:
#             subtotal = 0.0
#             for item in self.itemvenda_set.all():
#                 subtotal = float(subtotal) + float(str(item.valor_total_item.amount).replace(',', '.'))
#             subtotal = float(format(subtotal, '.2f'))
#             self.valor_total = Money(subtotal, 'BRL')
#         super(Venda, self).save(*args, **kwargs)


# class ItemVenda(TimeStamped):
#     class Meta:
#         verbose_name = u'Item de Venda'
#         verbose_name_plural = u'Itens de Venda'

#     venda = models.ForeignKey(Venda, on_delete=models.CASCADE, verbose_name='Venda ID')
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
#     valor_total_item = MoneyField(max_digits=14, blank=True, null=True, decimal_places=2, default_currency='BRL',
#                                   verbose_name='Valor do Item')
#     qtd = models.IntegerField(verbose_name='Quantidade', default=1)
#     desconto = models.CharField(max_length=5, blank=True, null=True, verbose_name='Desconto', default='0')

#     def __str__(self):
#         return u'Item: %s' % (self.pk)

#     def __unicode__(self):
#         return u'Item: %s' % (self.pk)

#     def save(self, *args, **kwargs):
#         if self.qtd and self.produto:
#             if self.qtd <= self.produto.qtd:
#                 self.produto.qtd = self.produto.qtd - self.qtd
#                 self.produto.save()
#                 subtotal = float(str(self.produto.valor_venda.amount).replace(',', '.')) * float(self.qtd)
#                 subtotal = float(format(subtotal, '.2f'))
#                 if self.desconto:
#                     if float(self.desconto) > 0:
#                         subtotal = subtotal - (subtotal * (float(self.desconto) / 100))
#                 self.valor_total_item = Money(subtotal, 'BRL')
#             else:
#                 raise ValueError(
#                     "Quantidade maior que o estoque disponivel."
#                 )
#         super(ItemVenda, self).save(*args, **kwargs)

# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Categoria(TimeStamped):
    categoria = models.CharField(max_length=200, blank=True, null=True, verbose_name='Categoria')

    def __str__(self):
        return "%s" % self.categoria

    def __unicode__(self):
        return "%s" % self.categoria


class Email(TimeStamped):
    email = models.EmailField()


class Tag(TimeStamped):
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tag')

    def __str__(self):
        return "%s" % self.tag

    def __unicode__(self):
        return "%s" % self.tag


class Post(TimeStamped):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    tags = models.ManyToManyField(Tag)
    link_download = models.URLField(blank=True, null=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    texto = RichTextField(config_name='awesome_ckeditor', blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)
    imagem_principal = models.URLField(blank=True, null=True)
    autor = models.CharField(max_length=300, blank=True, null=True, default='Caio Marinho')
    views = models.CharField(max_length=300, blank=True, null=True, default='385')
    comments = models.CharField(max_length=300, blank=True, null=True, default='12')

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return "%s" % self.titulo

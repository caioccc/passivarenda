from datetime import datetime, timedelta

from django import template

# from app.models import Venda, Entrada, Saida

register = template.Library()


def soma_val(values):
    v_total = 0.00
    if values:
        for v in values:
            v_total = v_total + float(v.valor)
    return round(v_total, 2)


@register.filter
def fix_money(valor):
    try:
        return str(valor).replace(',', '.')
    except (ValueError, ZeroDivisionError, Exception):
        return None


@register.filter
def vendas_totais(user):
    try:
        return Venda.objects.all().count()
    except (ValueError, ZeroDivisionError, Exception):
        return None


@register.filter
def vendas_mes(user):
    now = datetime.now()
    try:
        return Venda.objects.filter(created_at__month=now.month, created_at__year=now.year).count()
    except (ValueError, ZeroDivisionError, Exception):
        return None


@register.filter
def vendas_semana(user):
    now = datetime.now()
    try:
        start_date = now - timedelta(days=6)
        end_date = now
        return Venda.objects.filter(created_at__range=(start_date, end_date), created_at__year=now.year).count()
    except (ValueError, ZeroDivisionError, Exception):
        return None


@register.filter
def caixa_atual(user):
    try:
        entradas = Entrada.objects.all()
        saidas = Saida.objects.all()
        vendas = Venda.objects.all()
        caixa = 0
        for ent in entradas:
            caixa = float(caixa) + float(ent.valor)
        for venda in vendas:
            caixa = float(caixa) + float(venda.valor_total)
        for saida in saidas:
            caixa = float(caixa) - float(saida.valor)
        return caixa
    except (ValueError, ZeroDivisionError, Exception):
        return None

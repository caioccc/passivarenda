from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

# from app.models import Venda, Produto, Entrada, Saida


class HomeView(TemplateView):
    template_name = 'blog/index.html'

# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = 'painel/dashboard.html'
#     login_url = '/adminlogin/'

#     def get_context_data(self, **kwargs):
#         now = datetime.now()
#         kwargs['vendas'] = Venda.objects.all()
#         kwargs['produtos'] = Produto.objects.all().order_by('-lucro_aproximado')
#         entradas = Entrada.objects.filter(created_at__month=now.month, created_at__year=now.year)
#         saidas = Saida.objects.filter(created_at__month=now.month, created_at__year=now.year)
#         if entradas.count() > 0 and saidas.count() > 0:
#             kwargs['entradas'] = entradas
#             kwargs['saidas'] = saidas
#             kwargs['entradas_totais'] = self.get_totais(entradas,True,False,now)
#             kwargs['saidas_totais'] = self.get_totais(saidas,False,False,now)
#         else:
#             entradas = Entrada.objects.filter(created_at__month=now.month-1, created_at__year=now.year)
#             saidas = Saida.objects.filter(created_at__month=now.month-1, created_at__year=now.year)
#             kwargs['entradas'] = entradas
#             kwargs['saidas'] = saidas
#             kwargs['entradas_totais'] = self.get_totais(entradas, True, True, now)
#             kwargs['saidas_totais'] = self.get_totais(saidas, False, True, now)
#         return super(DashboardView, self).get_context_data(**kwargs)

#     def get(self, request, *args, **kwargs):
#         return super(DashboardView, self).get(request, *args, **kwargs)


#     def get_totais(self, lista, eh_entrada=False, eh_passado=False, now=datetime.now()):
#         sum = 0
#         if eh_entrada:
#             if eh_passado:
#                 vendas = Venda.objects.filter(created_at__month=now.month-1, created_at__year=now.year)
#             else:
#                 vendas = Venda.objects.filter(created_at__month=now.month, created_at__year=now.year)
#             for venda in vendas:
#                 sum = float(sum) + float(venda.valor_total)
#             for ent in lista:
#                 sum = float(sum) + float(ent.valor)
#         else:
#             for sai in lista:
#                 sum = float(sum) + float(sai.valor)
#         return sum
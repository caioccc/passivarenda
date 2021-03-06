#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class FormBaseAddress(BaseForm):
    cep = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'required': True,
                                                                       'maxlength': 200,
                                                                       'placeholder': 'CEP'
                                                                       }))
    endereco = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': True,
                                                                             'maxlength': 200,
                                                                             'placeholder': 'Endereço'
                                                                             }))
    numero = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'required': True,
                                                                         'maxlength': 200,
                                                                         'placeholder': 'Número'
                                                                         }))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True,
                                                                          'maxlength': 200,
                                                                          'placeholder': 'Bairro'
                                                                          }))

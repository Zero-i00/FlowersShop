from django.shortcuts import render
from django.views.generic import ListView
from core.models import *
from designer.forms.contact import ContactForm


class DesignerView(ListView):
    model = Flower
    success_url = '/'
    template_name = 'designer.html'
    context_object_name = 'flowers'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super(DesignerView, self).get_context_data(**kwargs)
        context['wrappers'] = Wrapper.objects.filter(in_stock=True)
        context['ribbons'] = Ribbon.objects.filter(in_stock=True)
        context['contact_form'] = ContactForm
        return context

    def get_queryset(self):
        return Flower.objects.filter(in_stock=True)
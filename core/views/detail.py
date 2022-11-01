from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.generic import FormView, DetailView
from core.forms import ContactForm
from core.models import Bouquet
from core.services.send_telegram_message import send_telegram_message
from django.core import serializers
from django.http.response import JsonResponse


class BouquetDetailView(DetailView):
    model = Bouquet
    success_url = '/'
    template_name = 'detail.html'
    context_object_name = 'bouquet'

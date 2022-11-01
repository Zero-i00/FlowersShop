from django.shortcuts import redirect
from django.views.generic import ListView
from core.forms import ContactForm
from core.models import Bouquet
from core.services.send_telegram_message import send_telegram_message


class AllBouquetsView(ListView):
    model = Bouquet
    success_url = '/'
    template_name = 'all_products.html'
    context_object_name = 'bouquets'
from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import FormView, ListView
from core.forms import ContactForm
from core.models import Bouquet
from core.services.send_telegram_message import send_telegram_message
from django.core import serializers
from django.http.response import JsonResponse


class HomeView(ListView):
    model = Bouquet
    success_url = '/'
    template_name = 'home.html'
    context_object_name = 'bouquets'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['quantity'] = Bouquet.objects.annotate(quantity_sum=Sum('quantity')).order_by('-quantity_sum').first()
        return context

    # def get_queryset(self):
    #     return Bouquet.objects.filter(in_stock=True)



# def user_info_list(request):
#     user_info = serializers.serialize(
#         'json',
#         UserInfo.objects.all(),
#         fields=('first_name', 'middle_name', 'last_name', 'position', 'gender', 'avatar', 'description')
#     )
#     return JsonResponse({'user_info': user_info}, status=200)

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.generic import FormView
from core.forms import ContactForm
from core.services.send_telegram_message import send_telegram_message
from django.core import serializers
from django.http.response import JsonResponse


class HomeView(FormView):
    form_class = ContactForm
    template_name = 'home.html'
    success_url = '/'

    def form_valid(self, form):
        send_telegram_message(form.data['full_name'], form.data['email'], form.data['phone'])
        return redirect(self.get_success_url())


# def user_info_list(request):
#     user_info = serializers.serialize(
#         'json',
#         UserInfo.objects.all(),
#         fields=('first_name', 'middle_name', 'last_name', 'position', 'gender', 'avatar', 'description')
#     )
#     return JsonResponse({'user_info': user_info}, status=200)

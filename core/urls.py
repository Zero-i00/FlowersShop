from django.urls import path, include
from django.conf.urls.static import static

from FlowersShop import settings
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', BouquetDetailView.as_view(), name='detail'),
    path('bouquets/all/', AllBouquetsView.as_view(), name='all_bouquets')
    # path('ajax/user_info', user_info_list, name='json_user_info__list')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from django.conf.urls.static import static

from FlowersShop import settings
from designer.views import DesignerView

urlpatterns = [
    path('', DesignerView.as_view(), name='designer'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

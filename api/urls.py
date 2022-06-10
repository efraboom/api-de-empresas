from django import conf
from django import urls
from django.urls import path
from .views import EmpresaView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('empresas/', EmpresaView.as_view(),name="empresa_list"),
    path('empresas/<int:id>', EmpresaView.as_view(),name="empresa_process")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
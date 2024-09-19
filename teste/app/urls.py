from django.urls import path
from .views import IndexView, DuvidaView

urlpatterns = [
    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # Página de dúvidas
    path('duvida/', DuvidaView.as_view(), name='duvida'),
]

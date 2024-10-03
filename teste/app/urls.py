from django.urls import path
from .views import IndexView

urlpatterns = [
    # Página inicial
    path('', IndexView.as_view(), name='index'),
]

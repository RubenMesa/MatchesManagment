from django.urls import path
from .views import posicionesview

urlpatterns=[
    path('posiciones/',posicionesview.as_view(),name='posiciones_list')
]
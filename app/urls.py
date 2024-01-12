# urls.py
from django.urls import path
from .views import purchase_order_view
urlpatterns = [
    # path('purchase_order/', GeneratePDF.as_view(), name='purchase_order'),
    path('generate_pdf/', purchase_order_view, name='generate_pdf'),

    # Add other URLs as needed
]

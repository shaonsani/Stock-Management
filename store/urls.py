from django.urls import path
from . import views
from .views import ProductAdd, ProductUpdate,History

app_name = 'APP'

urlpatterns = [
    path('',views.store, name='store'),
    path('sell/<int:pk>',views.sell, name='sell'),
    path('history/<str:data>',views.history,name='history'),
    path('add/',ProductAdd.as_view(), name='add_product'),
    path('update/<int:pk>',ProductUpdate.as_view(), name='update'),
    path('address/',views.address,name='address')
]

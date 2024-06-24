from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.item_list, name='list'),
    path('card/<int:item_id>/', views.item_card, name='card'),
]

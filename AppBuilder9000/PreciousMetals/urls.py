from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='PreciousMetals_home'),
    path('inventory/', views.inventory, name='PreciousMetals_inventory'),
    path('listing/', views.list_items, name='PreciousMetals_listing'),
    path('<id>', views.item_details, name='PreciousMetals_details'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
]

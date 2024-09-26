from django.urls import path
from .views import CreateItemEntry, UpdateItemQuantity, UnavailableItemsView, AllavailableItems

urlpatterns = [
    path('equipment/create/', CreateItemEntry.as_view(), name='create_item'),
    path('equipment/<int:pk>/update_quantity/', UpdateItemQuantity.as_view(), name='update_quantity'),
    path('equipment/unavailable/', UnavailableItemsView.as_view(), name='unavailable_items'),
    path('equipment/available/', AllavailableItems.as_view(), name='available_items'),
]

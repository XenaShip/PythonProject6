from django.urls import path
from .views import ContactsTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
]
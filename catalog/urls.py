from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ContactsTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, CategoriesListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
]
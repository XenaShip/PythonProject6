from django.views import generic
from catalog.models import Product
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm


class ContactsTemplateView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список товаров'
        template_name = 'catalog/product_list.html'
        return context_data


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        template_name = 'catalog/product_detail.html'
        return context_data


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    extra_context = {
        'title': 'Создание продукта'
    }


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Изменение продукта'
    }
    success_url = reverse_lazy('catalog:product_list')

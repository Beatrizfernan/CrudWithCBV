from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'trolley/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.count()
        return context
    


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'trolley/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'trolley/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'trolley/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from app_pages.forms import ContactModelForm
from app_pages.models import ContactModel


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class ProductsTemplateView(TemplateView):
    template_name = 'shop/product-list.html'


class ProductDetailTemplateView(TemplateView):
    template_name = ('shop/product-detail.html')


class UserWishlistTemplateView(TemplateView):
    template_name = ('shop/user-wishlist.html')


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel
    success_url = reverse_lazy('contact')  # Redirect to contact page after success

    def form_valid(self, form):
        pass
        # contact = form.save()
        # return super().form_valid(form)


    def form_invalid(self, form):
        pass
        # return super().form_invalid(form)

from django import forms

from app_pages.models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

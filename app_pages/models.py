from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.views import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128,verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(max_length=255,verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))


    def __str__(self):
        return f"{self.full_name},{self.subject}"


    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


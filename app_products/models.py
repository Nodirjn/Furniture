from django.db import models
from django.utils.translation import gettext_lazy as _
from app_common.views import BaseModel


class ColorModel(BaseModel):
    code = models.IntegerField(verbose_name=_('code'))
    name = models.CharField(max_length=125,verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')



class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=125,verbose_name=_('title'))
    parent = models.ForeignKey('self',
                               verbose_name=_('parent'),
                               null=True, blank=True,
                               on_delete=models.PROTECT,
                               related_name = 'children'
                               )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product category')
        verbose_name_plural = _('product categories')



class ProductTagModel(BaseModel):
    name = models.CharField(max_length=125,verbose_name=_('name'))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product tag')
        verbose_name_plural = _('product tags')


class ProductSizeModel(BaseModel):
    name = models.CharField(max_length=125,verbose_name=_('name'))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product size')
        verbose_name_plural = _('product sizes')




class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='products/',verbose_name=_('image1'))
    image2 = models.ImageField(upload_to='products/',verbose_name=_('image2'))
    title = models.CharField(max_length=125,verbose_name=_('title'))
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_('price'))
    description = models.TextField(verbose_name=_('description'))
    sku = models.CharField(max_length=125,verbose_name=_('sku'))


    colors = models.ManyToManyField(
        ColorModel,
        related_name='colors',
        verbose_name=_('colors')
         )

    tags = models.ManyToManyField(
        ProductTagModel,
        related_name='tags',
        verbose_name=_('tags')
        )

    categories = models.ManyToManyField(
        ProductCategoryModel,
        related_name='categories',
        verbose_name=_('categories')
        )
    sizes = models.ManyToManyField(
        ProductSizeModel,
        related_name='sizes',
        verbose_name=_('sizes')
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')




class ProductImageModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        related_name='images'
    )
    image = models.ImageField(upload_to='products/images/',verbose_name=_('image'))

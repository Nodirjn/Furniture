# Generated by Django 4.2.17 on 2025-01-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField(verbose_name='code')),
                ('name', models.CharField(max_length=125, verbose_name='name')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125, verbose_name='title')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='app_products.productcategorymodel', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'product category',
                'verbose_name_plural': 'product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125, verbose_name='name')),
            ],
            options={
                'verbose_name': 'product size',
                'verbose_name_plural': 'product sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125, verbose_name='name')),
            ],
            options={
                'verbose_name': 'product tag',
                'verbose_name_plural': 'product tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image1', models.ImageField(upload_to='products/', verbose_name='image1')),
                ('image2', models.ImageField(upload_to='products/', verbose_name='image2')),
                ('title', models.CharField(max_length=125, verbose_name='title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
                ('sku', models.CharField(max_length=125, verbose_name='sku')),
                ('categories', models.ManyToManyField(related_name='categories', to='app_products.productcategorymodel', verbose_name='categories')),
                ('colors', models.ManyToManyField(related_name='colors', to='app_products.colormodel', verbose_name='colors')),
                ('sizes', models.ManyToManyField(related_name='sizes', to='app_products.productsizemodel', verbose_name='sizes')),
                ('tags', models.ManyToManyField(related_name='tags', to='app_products.producttagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app_products.productmodel', verbose_name='product')),
            ],
        ),
    ]

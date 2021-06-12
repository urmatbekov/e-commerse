# Generated by Django 3.2.4 on 2021-06-12 12:31

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('description', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.TextField()),
                ('file', easy_thumbnails.fields.ThumbnailerImageField(upload_to='products')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.variation')),
            ],
        ),
    ]

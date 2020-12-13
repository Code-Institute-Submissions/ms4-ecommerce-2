# Generated by Django 3.1.3 on 2020-12-03 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='SKU', max_length=254)),
                ('gender', models.CharField(default='Men, Women, Unisex', max_length=25)),
                ('categories', models.CharField(default='Category', max_length=50)),
                ('sub_categories', models.CharField(blank=True, max_length=50)),
                ('brand', models.CharField(default='Band', max_length=50)),
                ('article_type', models.CharField(default='Article Type', max_length=150)),
                ('base_colour', models.CharField(blank=True, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('usage', models.CharField(blank=True, max_length=50)),
                ('product_name', models.CharField(default='Product Name', max_length=250)),
                ('description', models.TextField(default='Description')),
                ('image_url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
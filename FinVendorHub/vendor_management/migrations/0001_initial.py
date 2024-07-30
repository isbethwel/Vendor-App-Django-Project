# Generated by Django 4.2.11 on 2024-03-19 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('product_type', models.CharField(max_length=255)),
                ('documentation', models.FileField(blank=True, null=True, upload_to='product_docs/')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor_management.vendor')),
            ],
        ),
    ]
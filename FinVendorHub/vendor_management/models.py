from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    product_type = models.CharField(max_length=255)
    documentation = models.FileField(upload_to='product_docs/', blank=True, null=True)

    def __str__(self):
        return self.name

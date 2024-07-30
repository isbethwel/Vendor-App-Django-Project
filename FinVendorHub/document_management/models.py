from django.db import models
from vendor_management.models import Vendor, Product


class Document(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='documents', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='documents', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='vendor_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

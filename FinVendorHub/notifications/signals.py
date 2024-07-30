from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendor_management.models import Vendor
from django.conf import settings


@receiver(post_save, sender=Vendor)
def vendor_changed(sender, instance, created, **kwargs):
    subject = "Vendor Created" if created else "Vendor Updated"
    message = f"Vendor '{instance.name}' has been {'created' if created else 'updated'}."
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],  # Define ADMIN_EMAIL in your settings.py
    )

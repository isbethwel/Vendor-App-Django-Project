from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor, Product
from .forms import VendorForm, ProductForm


def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_management/vendor_list.html', {'vendors': vendors})


def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'vendor_management/vendor_detail.html', {'vendor': vendor})


def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendor_management/vendor_form.html', {'form': form})


def vendor_update(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor_management/vendor_form.html', {'form': form})


def vendor_delete(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    return render(request, 'vendor_management/vendor_confirm_delete.html', {'vendor': vendor})

from django.shortcuts import render
from vendor_management.models import Vendor
from document_management.models import Document


def search(request):
    query = request.GET.get('q', '')
    if query:
        vendor_results = Vendor.objects.filter(name__icontains=query)
        document_results = Document.objects.filter(title__icontains=query)
    else:
        vendor_results = []
        document_results = []

    return render(request, 'search/search_results.html', {
        'query': query,
        'vendor_results': vendor_results,
        'document_results': document_results
    })

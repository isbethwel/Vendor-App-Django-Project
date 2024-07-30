from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_management/document_list.html', {'documents': documents})


def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document_management/document_form.html', {'form': form})


def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'document_management/document_form.html', {'form': form})


def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document_management/document_confirm_delete.html', {'document': document})

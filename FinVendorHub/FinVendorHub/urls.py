"""
URL configuration for FinVendorHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from django.shortcuts import redirect
from accounts.views import register, login, logout
from vendor_management.views import vendor_list
from document_management.views import document_list
from search.views import search
from vendor_management import views as vendor_views
from document_management import views as document_views

# Your existing urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('vendors/', vendor_list, name='vendor_list'),
    path('documents/', document_list, name='document_list'),
    path('search/', search, name='search'),
    # Redirect from root to login
    re_path(r'^$', lambda request: redirect('login', permanent=False)),
    path('vendors/create/', vendor_views.vendor_create, name='vendor_create'),
    path('vendors/<int:pk>/', vendor_views.vendor_detail, name='vendor_detail'),
    path('vendors/<int:pk>/update/', vendor_views.vendor_update, name='vendor_update'),
    path('vendors/<int:pk>/delete/', vendor_views.vendor_delete, name='vendor_delete'),
    path('documents/', document_views.document_list, name='document_list'),
    path('documents/create/', document_views.document_create, name='document_create'),
    path('documents/<int:pk>/update/', document_views.document_update, name='document_update'),
    path('documents/<int:pk>/delete/', document_views.document_delete, name='document_delete'),
]
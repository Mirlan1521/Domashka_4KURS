"""kurs4_domahka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from magazin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.products_list),
    path('api/v1/products/<int:pk>/', views.products_item),
    path('api/v1/products/reviews/', views.product_reviews),
    path('api/v1/products/tags/', views.activ_tag_list_view)
]

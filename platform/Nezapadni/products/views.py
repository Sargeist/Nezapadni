from django.shortcuts import render





def index(request):
    context = {
    'title': 'Nezapadni'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
    'title': 'Produkty Nezapadni'
    }
    return render(request, 'products/products.html', context)
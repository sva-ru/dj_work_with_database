from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    name_sort = request.GET.get('sort')
    if name_sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif name_sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif name_sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}

    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).last()
    context = {'phone': phone}
    return render(request, template, context)

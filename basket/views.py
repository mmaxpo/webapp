from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST
from basket.models import Product, Basket

from basket.forms import BasketForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    form = BasketForm({'product': product.id})
    return render(request, 'product/product_detail.html', {'product': product, 'form': form})


@require_POST
def add_to_basket(request):
    response = render(request, 'basket/cart.html')
    basket_id = request.COOKIES.get('basket_id', None)

    if basket_id is None:
        basket = Basket.objects.create()
        response.set_cookie('basket_id', basket.id)
    else:
        try:
            basket = Basket.objects.get(pk=basket_id)
        except Basket.DoesNotExist:
            basket = Basket.objects.create()
            response.set_cookie('basket_id', basket.id)
    if request.user.is_authenticated:
        if basket.user is not None and basket.user != request.user:
            basket = Basket.objects.create(user=request.user)
            response.set_cookie('basket_id', basket.id)
        else:
            basket.user = request.user
            basket.save()
    form = BasketForm(request.POST)
    if form.is_valid():
        form.save(basket)
    # product_id = request.POST.get('product_id', None)
    # product_qty = request.POST.get('product_qty', 1)
    # if product_id is not None:
    #     try:
    #         product = Product.objects.get(id=product_id)
    #     except Product.DoesNotExist:
    #         raise Http404
    #     else:
    #         basket.add(product, product_qty)

    return response

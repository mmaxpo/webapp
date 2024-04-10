from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from shipping.forms import ShippingFrom
from django.views.decorators.http import require_POST


def shipping_list(request):
    return render(request, 'shipping/shipping_list.html')


@login_required
def shipping_create(request):
    if request.method == 'POST':
        form = ShippingFrom(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('shipping-list')
    else:
        form = ShippingFrom()
    return render(request, 'shipping/shipping_address.html', {'form': form})

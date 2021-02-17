from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ILqLhFp61B00rv29lDP3KeQATXO2yaa0W8pndnuPHTW4fuC35VmvVt6SDsQIPANB8l34cq3YPfN4ZRwq8PRwD1300AePS0QV2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

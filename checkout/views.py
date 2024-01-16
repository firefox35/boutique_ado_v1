from django.shortcuts import render
from django.contrib import messages

from .forms import Orderform

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51OYvEXEhOjsBBU1Hyd6YydpoCJQdABfKQ4gYMJqocP2Q4zG7nviXt161QHs51x4iu4NfuMQmFbaU6doKzyPWduId00MNcaWsM3',
            'client_secret': 'test client secret',
    }

    return render(request, template, context)

    
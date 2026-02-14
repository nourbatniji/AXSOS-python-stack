from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }

    return render(request, "store/index.html", context)


#handle postdata

def checkout(request):
    request.session['orders_total'] 
    request.session['total_quantity'] 

    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])

        product = Product.objects.get(id = request.POST['product_id'])
        print(product.price)




        quantity_counter = 0
        request.session['total_order_amount'] = float(product.price)
        request.session['orders_total'] += price_from_form * quantity_from_form
        request.session['total_quantity'] += quantity_counter + quantity_from_form

        Order.objects.create(quantity_ordered=quantity_from_form, total_price=quantity_from_form * price_from_form)
 
    return redirect('/thankyou')



def thankyou(request):

    context = {
        'total_order_amount' : request.session['total_order_amount'] ,
        'total_quantity_ordered' : request.session['total_quantity'],
        'total_of_order': request.session['orders_total']  
    }
    return render(request, 'store/checkout.html', context)
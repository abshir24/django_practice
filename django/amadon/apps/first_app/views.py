from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    count = 0
    if 'cart' in request.session:
        count = len(request.session['cart'])
    else:
        request.session['cart'] = []
    
    context = {
        'count':count
    }
    
    return render(request,"first_app/index.html", context)

def cart(request):
    product = {}
    if not request.POST['quantity'] == '0':
        product['price'] = float(request.POST['price']) * int(request.POST['quantity']) 
        product['name'] = request.POST['name']

    if product:
        cart = request.session['cart']
        cart.append(product)
        request.session['cart'] = cart

    return redirect('/')

def checkout(request):
    if len(request.session['cart']) == 0: 
        context = {
            'message' : "There are no items in your cart"
        }
        return render(request,"first_app/checkout.html",context)
    
    total=0; items = []
    
    for i in range(0,len(request.session['cart'])):
        total += request.session['cart'][i]['price']
        
        items.append(request.session['cart'][i]['name'])
    
    context = {
        'total':int(total),
        'items':items,
    }

    return render(request,"first_app/checkout.html",context)

def restart(request):
    request.session.flush()
    return redirect('/')
        
        
    

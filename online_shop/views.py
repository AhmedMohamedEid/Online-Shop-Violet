
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Count, Min,Sum

from .models import Setting , Categorie, product, Tag, Cart, Oreder
import json


context = {}
def context_base(request):
    context["categories"] = Categorie.objects.all()
    context["products"] = product.objects.all()
    return context

def index(request):
    context = context_base(request)
    return render(request, "index.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:

            return render(request, "login.html", {"message":"Invalid credentials."})
    else:
        return render(request, "login.html")


def categories(request):
    context = context_base(request)
    return render(request, "categories.html", context)

def subcategoies(request):
    context = context_base(request)
    return render(request, "categories.html", context)

def get_next_id(curr_id):
    try:
        ret = product.objects.filter(id__gt=curr_id).order_by("id")[0:1].get().id
    except product.DoesNotExist:
        ret = product.objects.aggregate(Min("id"))['id__min']
    return ret

def get_previous_id(curr_id):
    try:
        ret = product.objects.filter(id__lt=curr_id).order_by("id")[0:1].get().id
    except product.DoesNotExist:
        ret = product.objects.aggregate(Min("id"))['id__min']
    return ret

def product_page(request, id):
    context = context_base(request)
    context['product'] = product.objects.get(id=id)
    context["next_id"] = get_next_id(context['product'].id)
    context["previous_id"] = get_previous_id(context['product'].id)
    # print(get_previous_id(context['product'].id))
    print(context['product'].id)
    return render(request, "product-page.html",context)

def shopping_cart(request):
    context = context_base(request)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    # "total" : Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal')),
    cart = Cart.objects.filter(customer=request.user, finished=False)
    for c in cart:
        print(c.id)
        orders = Oreder.objects.filter(cart_id=c.id)
    context = {
        "cart" : cart,
        "items" : orders,

    }
    return render(request, "shopping-cart.html", context)


def add2chart(request):
    if not request.is_ajax: return { "success":False }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    cart = Cart.objects.filter(customer=request.user, finished=False)
    print(cart)
    if not cart:
        create_cart = Cart.objects.create(customer=request.user, ordered=True)
        create_cart.save()
        print("OK")
    else:
        create_cart = cart
    for c in cart:
        for item in items:

            print(item['id'])
            get_item = product.objects.get(pk=int(item['id']))
            cart_id = c
            product_id = get_item
            price = get_item.price
            quantity = 1
            subtotal = price*quantity
            order = Oreder.objects.create(product_id=product_id, cart_id=cart_id, price=price, quantity=quantity, subtotal=subtotal )
            order.save()

        c.shopping = 10
        c.subtotal = Oreder.objects.filter(cart_id=c.id).aggregate(Sum('subtotal'))
        c.total = c.subtotal['subtotal__sum'] + c.shopping
        cart.save()
        print(c.subtotal)


    return JsonResponse({"success":True, })



def calc_total(request):
    if not request.is_ajax: return { "success": False }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    date = {}
    for item in items:
        order = Oreder.objects.get(pk=int(item['id']))


        order.quantity = item['item_count']
        order.subtotal = item['subtotal']

        order.save()
        # total = Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal'))
        data = {'item_id': item['id'], "quantity":order.quantity, "subtotal":order.subtotal}

    print(data)
    return JsonResponse({"success":True, "data":data })

def clear_cart(request):
    if not request.is_ajax: return { "success": False }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    cart = Cart.objects.filter(customer=request.user, finished=False)
    for c in cart:
        order = Oreder.objects.filter(cart_id=c.id).delete()

    return JsonResponse({"success":True,})


def delete_order(request):
    if not request.is_ajax: return { "success": False }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    date = {}
    for item in items:
        order = Oreder.objects.get(pk=int(item['id'])).delete()

    return JsonResponse({"success":True, "data":data })

def checkout(request):
    return render(request, "check-out.html")



def contact_us(request):
    return render(request, "contact.html")

from django.shortcuts import redirect, render
from .models import Category, Product,Cart

def getCategory(request):
    categ = Category.objects.all()
    prod = Product.objects.all()
    context = {"category": categ, "product": prod}
    return render(request, "index.html", context)


def getOneCategory(request, category):
    categ = Category.objects.all()[:5]
    prod = Product.objects.filter(productType=category)
    context = {"category": categ, "product": prod}
    return render(request, "index.html", context)


def getOneProduct(request, id):
    categ = Category.objects.all()[:5]
    prod = Product.objects.get(id=id)
    item = [mm for mm in Product.objects.all() if mm != prod]
    context = {"category": categ, "item": prod,"product":item}
    return render(request, "OneProduct.html", context)


def addToCart(request,id):

    selected_product = Product.objects.get(id=id)
    cart_product = Cart(product=selected_product)
    cart_product.save()
    return redirect('getAllCart')


def getAllCart(request):
    items = Cart.objects.all()
    categ = Category.objects.all()[:5]
    context = {
        "category": categ,
        "cart":items
    }
    return render(request,"Cart.html",context)
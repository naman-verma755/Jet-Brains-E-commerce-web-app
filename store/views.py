from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import Product, Category, Customer, Order

from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

def home(request):
    return render(request,'home.html')



# Create your views here.
def index(request):
    products = None

    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {}
    data['products'] = products
    data['categories'] = categories
    if request.method == 'POST':
        remove_product = request.POST.get('product_remove')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if (cart):
            quantity = cart.get(product)
            if quantity:
                if remove_product:
                    if (quantity <= 1):
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = (quantity + 1)
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        #print(request.session['cart'])
        return render(request, 'product.html', data)

    # products = None
    #
    # products=Product.get_all_products()
    # categories= Category.get_all_categories()
    # data = {}
    # data['products'] = products
    # data['categories'] = categories
    return render(request, 'base.html', data)


def sign_up(request):
    categories = Category.get_all_categories()
    if request.method == 'GET':
        return render(request, 'signup.html', {'categories': categories})
    Post_data = request.POST
    first_name = Post_data.get('fname')
    last_name = Post_data.get('lname')
    email = Post_data.get('email')
    password = Post_data.get('pwd')

    error_message = None
    if (not first_name or len(first_name) == 0):
        error_message = "First Name required"
    elif (not first_name.isalpha()):
        error_message = "First Name should contain all characters"
    elif (not last_name or len(last_name) == 0):
        error_message = "Last Name required"
    elif (not last_name.isalpha()):
        error_message = "Last Name should contain all characters"

    value = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}

    if not error_message:
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password)

        customer.password = make_password(customer.password)
        customer.register_customer()

        return redirect("home")
    else:
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, "signup.html", data)

def url():
    return_url = None
    return return_url
class Log_in(View):
    return_url = None
    def get(self,request):
        Log_in.return_url = request.GET.get('return_url')

        return render(request, 'log_in.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_email(email)
        error_message = None
        if customer:
            if check_password(password, customer.password):
                request.session['customer'] = customer.id

                if Log_in.return_url:

                    return_url = None
                    return HttpResponseRedirect(Log_in.return_url)
                else:
                    return redirect('home')

            else:
                error_message = 'Invalid password'
        else:
            error_message = 'Email or Password invalid'
        return render(request, 'log_in.html', {'error': error_message})


def log_out(request):
    request.session.clear()
    return redirect('login')


def cart(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        #print(products)
        return render(request, 'cart.html', {'products': products})


def product(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        #print('product', product)
        return redirect("home")
    else:
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None

        #print("yes")
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if (category_id):
            products = Product.products_by_id(category_id)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'product.html', data)


def checkout(request):
    if request.method == 'GET':
        return render(request, "checkout.html")
    else:
        Request = request.POST
        first_name = Request.get('f_name')
        last_name = Request.get('l_name')
        Address = Request.get('address')
        State = Request.get('state')
        Zip = Request.get('zip')
        Phone = Request.get('phone')
        Email = Request.get('email')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        customer = request.session.get('customer')
       # print(first_name, last_name, Address, State, Zip, Phone, Email, cart, products)
        for product in products:
            order = Order(customer=Customer(id=customer),
                          first_name=first_name,
                          last_name=last_name,
                          address=Address,
                          state=State,
                          zip=Zip,
                          phone=Phone,
                          email=Email,
                          quantity=cart.get(str(product.id)),
                          product=product,
                          price=product.price,
                          )
            order.placeOrder()
        request.session['cart'] = {}

        return redirect('cart')

class order_view(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'order.html', {'orders': orders})
        #print('orders=',orders)
#
#     return render(request,'order.html', {'orders':orders})

    # if(request.method == 'GET'):
    #
    #     customer = request.session.get('customer')
    #     orders = Order.get_orders_by_customer(customer)
    #     #print('orders=',orders)
    #
    #     return render(request,'order.html', {'orders':orders})
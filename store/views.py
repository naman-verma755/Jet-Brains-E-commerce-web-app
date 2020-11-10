from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Customer
# Create your views here.
def index(request):
    products = Product.get_all_products()
    categories= Category.get_all_categories()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'base.html',data)


def sign_up(request):
    categories = Category.get_all_categories()
    if request.method == 'GET':
        return render(request,'signup.html',{'categories':categories})
    Post_data = request.POST
    first_name = Post_data.get('fname')
    last_name = Post_data.get('lname')
    email = Post_data.get('email')
    password = Post_data.get('pwd')
    print(first_name,last_name,email,password)
    customer = Customer(first_name = first_name,
                        last_name = last_name,
                        email = email,
                        password = password)
    customer.register_customer()
    return HttpResponse('Sign Up success')

def product(request):
    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if(category_id):
        products = Product.products_by_id(category_id)
    else:
        products = Product.get_all_products()


    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'product.html',data)


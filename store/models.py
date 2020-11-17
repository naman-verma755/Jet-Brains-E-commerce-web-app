from django.db import models
import  datetime

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=2000,default="")
    image = models.ImageField(upload_to='uploads/product_images/')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod

    def products_by_id(category_id):
        if(category_id):
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # phone = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register_customer(self):
        self.save()
    @staticmethod
    def get_customer_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
    def is_already_exists(self):
        if( Customer.objects.filter(email=self.email)):
            return True
        return False


class Order(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    first_name = models.CharField(max_length=100,default = "",blank=True)
    last_name = models.CharField(max_length=100,default="",blank=True)
    zip = models.IntegerField(default=0)
    city = models.CharField(max_length=100,default="",blank=True)
    state = models.CharField(max_length=100,default="",blank=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=200,default='',blank=True)
    phone = models.CharField(max_length=15,default=0,blank=True)
    date = models.DateField(default=datetime.datetime.today)
    email = models.EmailField(default="")
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')


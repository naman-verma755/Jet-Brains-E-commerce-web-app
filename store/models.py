from django.db import models
import  datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    #new fields
    image = models.ImageField(upload_to='uploads/product_images/',blank=True)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    brand = models.CharField(max_length=100,default='')
    type = models.CharField(max_length=100,default='')
    keyword = models.CharField(max_length=1000,default='')
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
        Dict = dict()
        if(category_id):
            Dict['category']=category_id

        print('Here')
        for i in Dict:
            print(i,Dict[i])
        if(category_id):
            return Product.objects.filter(**Dict)
        else:
            return Product.objects.all()
        # category = category_id, brand = 'None'
    # @staticmethod
    # def filter_by_price():
    #     print(Product.objects.filter(category = price))


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


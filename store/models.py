from django.db import models


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



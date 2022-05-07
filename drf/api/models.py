from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, default='Almaty')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['id']
        
class Category(models.Model):
    category_name = models.CharField(max_length=100, default=0) 
    icon = models.ImageField()
    #parent = models.ForeignKey('self' , on_delete= models.CASCADE)
    
    def __str__(self): 
        return self.category_name 
    
class Products(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits= 7, decimal_places=2)
    image = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add = True)
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.product_name
    
    class Meta: 
        ordering= ['-upload_date']
    


        

    
from django.db import models

class Book(models.Model):
    bookid = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=200)    
    author = models.CharField(max_length=200)   
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    total_quantity = models.IntegerField(default=1) 
    issued = models.IntegerField(default=0)     
    publisher = models.CharField(max_length=200, default="Unknown Publisher")  
    language = models.CharField(max_length=50, default="English") 

    def __str__(self):
        return f"{self.name} by {self.author}"

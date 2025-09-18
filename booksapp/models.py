from django.db import models

# Book model
class Book(models.Model):
    bookid = models.IntegerField(unique=True)  
    name = models.CharField(max_length=200)   
    author = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=6, decimal_places=2)  

    def __str__(self):
        return f"{self.name} by {self.author}"

from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_data  = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    descriptoin = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)


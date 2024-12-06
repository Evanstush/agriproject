from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length =30)
    lname = models.CharField(max_length =30)
    email = models.EmailField()
    phone = models.CharField(max_length =30)
    county = models.CharField(max_length =30)
    message = models.TextField()

    def __str__(self):
        return self.fname
class Admin(models.Model):
    username = models.CharField(max_length =30)
    password = models.CharField(max_length =30)

    def __str__(self):
        return self.username

class Register_courses(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()
    phone = models.CharField(max_length =30)
    gender = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    course = models.CharField(max_length =30)
    hours = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Farmers(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()
    phone = models.CharField(max_length =30)
    password = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Customers(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()
    phone = models.CharField(max_length =30)
    password = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField()
    price = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/')
    def __str__(self):
        return self.title


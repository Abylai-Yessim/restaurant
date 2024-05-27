from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'menu_images/{new_file_name}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(blank=True, upload_to=uniq_name_upload)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    text = models.TextField()  
    
class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    cart_items = models.ManyToManyField(MenuItem, blank=True)

class SiteSettings(models.Model):
    times = models.TextField(max_length=50,default='')
    booking_button_text = models.CharField(max_length=50, default='Забронировать')

    def __str__(self):
        return 'Site Settings'

class Table(models.Model):
    number = models.IntegerField(unique=True)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.number}'

class TableDetails(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.DateTimeField()
    
    def __str__(self):
        return f'Table {self.table.number} - {self.time}'

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    table_number = models.IntegerField()
    time = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Booking for Table {self.table_number} at {self.time} by {self.phone}"

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number
    
class ReservedTable(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.table} - {self.time}"

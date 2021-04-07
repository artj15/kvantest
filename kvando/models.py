from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, default= 'Имя')
    last_name = models.CharField(max_length=50, default= 'Фамилия')
    phone_number = models.CharField(max_length=15, 'Номер телефона')

from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, default= 'Имя')
    last_name = models.CharField(max_length=50, default= 'Фамилия')
    phone_number = models.CharField(max_length=15, default = 'Номер телефона')
    def __str__(self):
        return f"Имя {self.first_name}, Фамилия {self.last_name}, Телефон {self.phone_number}"
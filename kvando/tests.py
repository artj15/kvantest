from django.test import TestCase
from .models import  Contact

# Create your tests here.

class TestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.object.create(country_code = '+7', first_name = 'Тест', last_name = 'Тестов', phone_number = '152633654')

    def country(self):
        contact = Contact.object.get()
        print(contact)
        contact_label = contact._meta.get_field('country_code').verbose_name
        self.assertEquals(contact_label, 'country_code')

    def first_name(self):
        contact = Contact.object.get()
        print(contact)
        contact_label = contact._meta.get_field('first_name').verbose_name
        self.assertEquals(contact_label, 'first_name')

    def last_name(self):
        contact = Contact.object.get()
        print(contact)
        contact_label = contact._meta.get_field('last_name').verbose_name
        self.assertEquals(contact_label, 'last_name')

    def last_name(self):
        contact = Contact.object.get()
        print(contact)
        contact_label = contact._meta.get_field('phone_number').verbose_name
        self.assertEquals(contact_label, 'phone_number')

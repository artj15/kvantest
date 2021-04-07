from django.urls import path
from .views import ContactList, ContactDetailViewFirstName, ContactDetailViewPhoneNumber

urlpatterns =[
    path('', ContactList.as_view()),
    path('<first_name>', ContactDetailViewFirstName.as_view()),
    path('<phone_number>', ContactDetailViewPhoneNumber.as_view()),
]
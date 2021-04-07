from django.urls import path
from .views import ContactList, ContactDetailView, ContactDetailViewNumber

urlpatterns =[
    path('', ContactList.as_view()),
    path('<Имя>', ContactDetailView.as_view()),
    path('<Номер>', ContactDetailViewNumber.as_view()),
]
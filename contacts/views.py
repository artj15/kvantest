from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
from django.views.generic import  TemplateView
# Create your views here.

class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)


class ContactDetailViewFirstName(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    lookup_field = 'first_name'

    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)

class ContactDetailViewPhoneNumber(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    lookup_field = 'phone_number'

    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)


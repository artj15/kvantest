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


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    lookup_field = 'id'

    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)


class List(TemplateView):
    template_name = 'contactlist.html'
    def get(self, request):
        all_contacts = List.objects.all()


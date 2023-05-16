from django.http import Http404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import PersonForm
from django.views.generic import FormView
from django.shortcuts import redirect


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['pk', 'name', 'last_name', 'created_at']


class UserAll(APIView):
    """   UserAll shows all users that are in the database   """

    def get(self, *args, **kwargs):
        users = Person.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)


class PersonDetailView(APIView):
    """   PersonDetainView gets the person behind the PC in json format   """

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = UserSerializer(person)
        return Response(serializer.data)


class GetUser(FormView):
    """   The user fills out the form and after GetUser adds it to the database   """

    form_class = PersonForm
    template_name = 'party/home.html'

    def form_valid(self, form):
        cd = form.cleaned_data
        person = Person(name=cd.get('name'), last_name=cd.get('last_name'))
        person.save()
        return redirect('new_url', pk=person.pk)

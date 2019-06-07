from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person



# Create your views here.

@api_view()
def person(request):
	person_list=Person.objects.all()
	return Response({"data":person_list})































		


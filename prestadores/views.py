import pytz
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PersonSerializer, SupplierSerializer, ExpertiseSerializer
from urllib.request import urlopen


from .models import Person, Expertise, Supplier

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'prestadores/signup.html'

def index(request):
    template = loader.get_template('prestadores/index.html')

    context = {}

    return HttpResponse(template.render(context, request))

def person (request, person_id):
    person_obj = Person.objects.get(pk=person_id)
    template = loader.get_template('prestadores/person.html')
    context = {
        'id': person_obj.id,
        'name': person_obj.name,
        'insertion_date': person_obj.insertion_date
    }

    return HttpResponse(template.render(context, request))

@api_view(['POST'])
def create_person(request):
    person_serializer = PersonSerializer(data=request.data)
    if person_serializer.is_valid():
        person_serializer.save()
        return Response({"data": "Person added successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in person_serializer.errors.keys():
            error_details.append({"field": key, "message": person_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_person(request, person_id):
    person_obj = Person.objects.get(pk=person_id)
    person_serializer = PersonSerializer(person_obj, data=request.data)
    if person_serializer.is_valid():
        person_serializer.save()
        return Response({"data": "Person updated successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in person_serializer.errors.keys():
            error_details.append({"field": key, "message": person_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

def delete_person(request, person_id):
    person_obj = Person.objects.get(pk=person_id)
    template = loader.get_template('prestadores/delete_person.html')
    Person.objects.filter(pk=person_id).update(exclusion_date=timezone.now())
    context = {
        'id': person_obj.id
    }

    return HttpResponse(template.render(context, request))

@api_view(['DELETE'])
def delete_person_api(request, person_id):
    person_obj = Person.objects.get(pk=person_id)
    person_obj.exclusion_date=timezone.now()

    return HttpResponse(status=204)

def retrieve_persons(request):
    persons_list = Person.objects.filter(exclusion_date__isnull=True).order_by('-insertion_date')[:5]
    template = loader.get_template('prestadores/retrieve_persons.html')
    context = {
        'persons_list': persons_list,
    }

    return HttpResponse(template.render(context, request))


class ActivePersonsList(generics.ListCreateAPIView):
    queryset = Person.objects.filter(exclusion_date__isnull=True).order_by('-insertion_date')
    serializer_class = PersonSerializer

class AllPersonsList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


def supplier (request, person_id):
    supplier_obj = Supplier.objects.get(pk=person_id)
    person_obj = Person.objects.get(pk=person_id)
    template = loader.get_template('prestadores/supplier.html')
    context = {
        'id': person_id,
        'insertion_date': supplier_obj.insertion_date
    }
    return HttpResponse(template.render(context, request))

@api_view(['POST'])

def create_supplier(request):
    supplier_serializer = SupplierSerializer(data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response({"data": "Supplier added successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in supplier_serializer.errors.keys():
            error_details.append({"field": key, "message": supplier_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_supplier(request, supplier_id):
    supplier_obj = Supplier.objects.get(pk=supplier_id)
    supplier_serializer = SupplierSerializer(supplier_obj, data=request.data)
    if supplier_serializer.is_valid():
        supplier_serializer.save()
        return Response({"data": "Supplier updated successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in supplier_serializer.errors.keys():
            error_details.append({"field": key, "message": supplier_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

def delete_supplier(request, supplier_id):
    supplier_obj = Supplier.objects.get(pk=supplier_id)
    supplier_obj.exclusion_date=timezone.now()
    return HttpResponse(status=204)

def retrieve_suppliers(request):
    return HttpResponse("In development...Here are all suppliers")

def expertise (request, person_id):
    expertise_obj = Expertise.objects.get(pk=person_id)
    person_obj = Person.objects.get(pk=person_id)
    template = loader.get_template('prestadores/expertise.html')
    context = {
        'id': person_id,
        'insertion_date': expertise_obj.insertion_date,
        'field': expertise_obj.field
    }
    return HttpResponse(template.render(context, request))

@api_view(['POST'])
def create_expertise(request):
    expertise_serializer = ExpertiseSerializer(data=request.data)
    if expertise_serializer.is_valid():
        expertise_serializer.save()
        return Response({"data": "Expertise added successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in expertise_serializer.errors.keys():
            error_details.append({"field": key, "message": expertise_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_expertise(request, expertise_id):
    expertise_obj = Expertise.objects.get(pk=expertise_id)
    expertise_serializer = ExpertiseSerializer(expertise_obj, data=request.data)
    if expertise_serializer.is_valid():
        expertise_serializer.save()
        return Response({"data": "Expertise updated successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in expertise_serializer.errors.keys():
            error_details.append({"field": key, "message": expertise_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

def delete_expertise(request, expertise_id):
    expertise_obj = Expertise.objects.get(pk=expertise_id)
    expertise_obj.exclusion_date=timezone.now()
    return HttpResponse(status=204)

def retrieve_expertises(request):
    return HttpResponse("In development...Here are all expertises")

class AllExpertiseList(generics.ListCreateAPIView):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer

class AllSuppliersList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

def search_persons (request):
    if request.method == 'GET':
        active_persons_list = Person.objects.filter(name__istartswith= request.GET.get('search_box', None), exclusion_date__isnull=True).order_by('-insertion_date')[:5]
        active_suppliers_list = Supplier.objects.filter(person__name__istartswith = request.GET.get('search_box', None), exclusion_date__isnull=True).order_by('-insertion_date')[:5]
        #active_expertise_list = Expertise.objects.filter(supplier__person__name_istartswith = request.GET.get('search_box', None))
        template = loader.get_template('prestadores/search_persons.html')
        context = {
            'active_persons_list': active_persons_list,
            'active_suppliers_list': active_suppliers_list,
           # 'active_expertise_list': active_expertise_list,
        }
    return HttpResponse(template.render(context, request))

def get_awards(request):
    url = "https://jns-filmes.herokuapp.com/api/awards"
    with urlopen(url) as conn:
        json_url = urlopen(url)
        data = json.loads(json_url.read())
        template = loader.get_template('prestadores/get_awards.html')
        context = {
            'data': data
        }
    
    return HttpResponse(template.render(context, request))

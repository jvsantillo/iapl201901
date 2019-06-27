import pytz
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from .serializers import PersonSerializer, SupplierSerializer, ExpertiseSerializer


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

def create_person(request):
    request.GET('')
    return HttpResponse("In development... You are creating a person")
def update_person(request, person_id):
    return HttpResponse("In development... You are updating person ID %s." % person_id)

def delete_person(request, person_id):
    person_obj = Person.objects.get(pk=person_id)
    template = loader.get_template('prestadores/delete_person.html')
    print(person_obj.exclusion_date, person_obj.name)
    Person.objects.filter(pk=person_id).update(exclusion_date=timezone.now())
    print(person_obj.exclusion_date)
    context = {
        'id': person_obj.id
    }
    return HttpResponse(template.render(context, request))

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

def create_supplier(request):
    return HttpResponse("In development... You are creating a supplier")
def update_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
def delete_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
    return HttpResponse("In development... You are deleting supplier ID %s." % supplier_id)
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

def create_expertise(request):
    return HttpResponse("In development... You are creating a expertise")
def update_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
def delete_expertise(request, expertise_id):
    return HttpResponse("In development... You are updating expertise ID %s." % expertise_id)
    return HttpResponse("In development... You are deleting expertise ID %s." % expertise_id)
def retrieve_expertises(request):
    return HttpResponse("In development...Here are all expertises")

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

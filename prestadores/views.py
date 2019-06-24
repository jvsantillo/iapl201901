import pytz
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone


from .models import Person

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

def supplier (request, supplier_id):
    return HttpResponse("You are looking at supplier %s" % supplier_id)
def create_supplier(request):
    return HttpResponse("In development... You are creating a supplier")
def update_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
def delete_supplier(request, supplier_id):
    return HttpResponse("In development... You are updating supplier ID %s." % supplier_id)
    return HttpResponse("In development... You are deleting supplier ID %s." % supplier_id)
def retrieve_suppliers(request):
    return HttpResponse("In development...Here are all suppliers")

def expertise (request, expertise_id):
    return HttpResponse("You are looking at expertise %s" % expertise_id)
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
        active_persons_list = Person.objects.filter(name__contains= request.GET.get('search_box', None), exclusion_date__isnull=True).order_by('-insertion_date')[:5]
        template = loader.get_template('prestadores/search_persons.html')
        context = {
            'active_persons_list': active_persons_list,
        }
    return HttpResponse(template.render(context, request))
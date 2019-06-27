from django.urls import path, include 


from . import views

urlpatterns = [
    #ex: /prestadores/
    path('', views.index, name='index'),
    #ex: /prestadores/create_peson
    path('create_person/', views.create_person, name='create_person'),
    #ex: /prestadores/person/1
    path('person/<int:person_id>/', views.person, name='person'),
    #ex: /prestadores/update_person/1
    path('update_person/<int:person_id>/', views.update_person, name='update_person'),
    #ex: /prestadores/delete_person/1
    path('delete_person/<int:person_id>/', views.delete_person, name='delete_person'),
    #ex: /prestadores/retrieve_persons
    path('retrieve_persons/', views.retrieve_persons, name='retrieve_persons'),
    

    #ex: /prestadores/create_supplier
    path('create_supplier/', views.create_supplier, name='create_supplier'),
    #ex: /prestadores/supplier/1
    path('supplier/<int:person_id>/', views.supplier, name='supplier'),
    #ex: /prestadores/update_supplier/1
    path('update_supplier/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    #ex: /prestadores/delete_supplier/1
    path('delete_supplier/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
    #ex: /prestadores/retrieve_suppliers
    path('retrieve_suppliers/', views.retrieve_suppliers, name='retrieve_suppliers'),

    #ex: /prestadores/create_expertise
    path('create_expertise/', views.create_expertise, name='create_expertise'),
    #ex: /prestadores/expertise/1
    path('expertise/<int:person_id>/', views.expertise, name='expertise'),
    #ex: /prestadores/update_expertise/1
    path('update_expertise/<int:expertise_id>/', views.update_expertise, name='update_expertise'),
    #ex: /prestadores/delete_expertise/1
    path('delete_expertise/<int:expertise_id>/', views.delete_expertise, name='delete_expertise'),
    #ex: /prestadores/retrieve_expertises
    path('retrieve_expertises/', views.retrieve_expertises, name='retrieve_expertises'),

    #ex: /prestadores/search_persons
    path('search_persons/', views.search_persons, name='search_persons'),
    #ex: /prestadores/signup
    path('signup/', views.SignUp.as_view(), name='signup'),

    #API REST:

    #ex: /prestadores/api/active_persons_list
    path('api/active_persons_list', views.ActivePersonsList.as_view(), name='active_persons_list'),
    #ex: /prestadores/api/active_persons_list
    path('api/all_persons_list', views.AllPersonsList.as_view(), name='all_persons_list')

]
from rest_framework import serializers
from .models import Person, Supplier, Expertise

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        person_obj = Person(**validated_data)
        person_obj.save()
        return person_obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.insertion_date = validated_data.get('insertion_date', instance.insertion_date)
        instance.exclusion_date = validated_data.get('exclusion_date', instance.exclusion_date)
        instance.save()
        return instance

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
    
    def create(self, validated_data):
        supplier_obj = Supplier(**validated_data)
        supplier_obj.save()
        return supplier_obj

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.insertion_date = validated_data.get('insertion_date', instance.insertion_date)
        instance.exclusion_date = validated_data.get('exclusion_date', instance.exclusion_date)
        instance.save()
        return instance

class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'

    def create(self, validated_data):
        expertise_obj = Expertise(**validated_data)
        expertise_obj.save()
        return expertise_obj

    def update(self, instance, validated_data):
        instance.field = validated_data.get('field', instance.field)
        instance.description = validated_data.get('description', instance.description)
        instance.suppliers = validated_data.get('suppliers', instance.suppliers)
        instance.insertion_date = validated_data.get('insertion_date', instance.insertion_date)
        instance.exclusion_date = validated_data.get('exclusion_date', instance.exclusion_date)
        instance.save()
        return instance
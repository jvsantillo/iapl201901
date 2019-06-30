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
        instance.name = validated_data["name"]
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
        instance.name = validated_data["name"]
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
        instance.name = validated_data["name"]
        instance.save()
        return instance
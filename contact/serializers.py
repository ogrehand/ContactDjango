from rest_framework import serializers
from contact.models import Person, Contacts
"""
class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=50)
"""

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'description']

"""
class ContactsSerializer(serializers.Serializer):
    person_id = serializers.ForeignKey(Person, on_delete=models.CASCADE)
    contactType = serializers.CharField(max_length=15,blank=True,default='')
    contactid = serializers.CharField(max_length=30)
"""


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['personId', 'contactType', 'contactId']
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from contact.models import Person, Contacts
from contact.serializers import PersonSerializer, ContactsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Create your views here.


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'persons': reverse('user-list', request=request, format=format),
#         'contacts': reverse('snippet-list', request=request, format=format)
#     })

class PersonList(APIView):
    def get(self, request, format=None):
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContacsOnlyList(APIView):
    def get(self, request, format=None):
        snippets = Contacts.objects.all()
        serializer = ContactsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactsList(APIView):
    """
    List all snippets, or create a new snippet.
    """ 
    def get_object(self, PersonId):
        try:
            return Contacts.objects.get(personId=PersonId)
        except Person.DoesNotExist:
            raise Http404

    # def get(self, request, format=None):
    #     snippets = Contacts.objects.all()
    #     serializer = ContactsSerializer(snippets, many=True)
    #     return Response(serializer.data)

    def get(self, request, PersonId, format=None):
        snippet = self.get_object(PersonId)
        serializer = ContactsSerializer(snippet)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, PersonId, format=None):
        snippet = self.get_object(PersonId)
        serializer = ContactsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, PersonId, format=None):
        snippet = self.get_object(PersonId)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
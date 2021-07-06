from django.urls import path
from contact import views


urlpatterns = [
    path('person/', views.PersonList.as_view()),
    path('contacts/', views.ContacsOnlyList.as_view()),
    path('contacts/<int:PersonId>/', views.ContactsList.as_view()),
    # path('contactslist/<str:PersonId>/', views.ContactsList.as_view()),
]
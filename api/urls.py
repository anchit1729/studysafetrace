from django.urls import path
from api import views

urlpatterns = [
    path('contacts/<str:uid>/<str:date>', views.ViewContacts.as_view(), name='view-contacts'),
    path('venues/<str:uid>/<str:date>', views.ViewVenues.as_view(), name='view-contacts')
]

from django.shortcuts import render
from django.views.generic import TemplateView
import json
import requests
from datetime import datetime, timedelta


# Class-based view with template
class ViewContacts(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        core_endpoint = "https://tranquil-everglades-00058.herokuapp.com/"
        uid = self.kwargs['uid']
        date = self.kwargs['date']
        core_endpoint += 'api/contacts/' + uid + '/' + date

        r = requests.get(core_endpoint)
        # a list of json dictionary containing close-contact information
        contacts_json = r.json()
        contacts = [contact['uid'] for contact in contacts_json]

        context['subject'] = uid
        context['contacts'] = contacts

        return context


class ViewVenues(TemplateView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        core_endpoint = "https://tranquil-everglades-00058.herokuapp.com/"
        uid = self.kwargs['uid']
        date = self.kwargs['date']
        core_endpoint += 'api/venues/' + uid + '/' + date

        r = requests.get(core_endpoint)
        # a list of json dictionary containing close-contact information
        venues_json = r.json()
        venues = [venue['venue_code'] for venue in venues_json]

        context['subject'] = uid
        context['venues'] = venues

        return context

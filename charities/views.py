from django.shortcuts import render
from django.views.generic import CreateView

from charities.forms import CreateCharityForm


class CreateCharityView(CreateView):
    form_class = CreateCharityForm
    template_name = 'charities/create_charity.html'

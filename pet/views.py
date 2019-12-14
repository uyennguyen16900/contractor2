from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from pet.models import Pet
from pet.forms import PetForm
from django.utils import timezone
from datetime import datetime

class PetListView(ListView):
    """ Renders a list of all Pets. """
    model = Pet

    def get(self, request):
        """ GET a list of Pets. """
        pets = self.get_queryset().all()
        return render(request, 'list.html', {
          'pets': pets
        })

class PetDetailView(DetailView):
    """ Renders a specific page based on pet's slug."""
    model = Pet

    def get(self, request, slug):
        """ Returns a specific pet page by slug. """
        pet = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'pet.html', {
          'pet': pet
        })

class PetAddView(CreateView):
    """Add new pet to the list"""
    model = Pet
    form_class = PetForm
    template_name = 'add.html'

    def post(self, request):
        form = PetForm(request.POST)
        form.instance.owner = self.request.user
        if form.is_valid():
            pet = form.save()
            return redirect('pet-details-page', slug=pet.slug)

class PetEditView(UpdateView):
    """Update a pet's information"""
    model = Pet
    fields = '__all__'
    template_name = 'edit.html'

    def form_valid(self, form):
        pet = form.save()
        return redirect('pet-details-page', slug=pet.slug)

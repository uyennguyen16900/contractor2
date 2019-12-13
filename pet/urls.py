from django.urls import path
from pet.views import PetListView, PetDetailView, PetEditView, PetAddView

urlpatterns = [
    path('', PetListView.as_view(), name='pet-list-page'),
    path('<str:slug>', PetDetailView.as_view(), name='pet-details-page'),
    path('<str:slug>/edit', PetEditView.as_view(), name='pet-edit-page'),
    path('add/', PetAddView.as_view(), name='pet-add-page')

]

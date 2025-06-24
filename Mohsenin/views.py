from django.shortcuts import render, get_object_or_404, redirect  
from django.views import View  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  
from django.urls import reverse_lazy  
from .models import Family, Dist, Person
from .forms import FamilyForm, NewFamilyForm, DistForm, PersonForm

# Create your views here.

def index(request):
    return render(request, 'Mohsenin/index.html')

#-------------- Distribution list views
class DistListView(ListView):
    model = Dist
    template_name = 'Dist/Dist_list.html'
    context_object_name = 'dists'

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        return context


class DistCreateView(CreateView):
    model = Dist
    form_class = DistForm
    template_name = 'Dist/Dist_form.html'
    success_url = reverse_lazy('dist_list')

class DistUpdateView(UpdateView):  
    model = Dist  
    form_class = DistForm  # Use a ModelForm for Family  
    template_name = 'Dist/Dist_form.html'  
    success_url = reverse_lazy('dist_list')

class DistDeleteView(View):  
    def get(self, request, pk):  
        dist = get_object_or_404(Dist, pk=pk)  
        return render(request, 'Dist/dist_confirm_delete.html', {'dist': dist})  
    
    def post(self, request, pk):  
        dist = get_object_or_404(Dist, pk=pk)  
        dist.delete()  
        return redirect(reverse_lazy('dist_list'))
 


#-------------- Observation views
class ObservationListView(View):  
    def get(self, request, family_id):  
        family = get_object_or_404(Family, id=family_id)  
        observations = family.observation_set.all()  
        return render(request, 'observations/observation_list.html', {'family': family, 'observations': observations})  

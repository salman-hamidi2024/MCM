from django.shortcuts import render, get_object_or_404, redirect  
from django.views import View  
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy  
from ..models import Family, Person, Family_Type
from ..forms import FamilyForm, NewFamilyForm,PersonForm
#------------ Family views
class FamilyListView(ListView):  
    model = Family  
    template_name = 'Family/family_list.html'  
    context_object_name = 'families'

    def get_queryset(self):  
        queryset = super().get_queryset()  
        
 

        # Filter by active/inactive  
        active_filter = self.request.GET.get('active_filter')  
        if active_filter == 'active':  
            queryset = queryset.filter(is_active=True)  
        elif active_filter == 'not_active':  
            queryset = queryset.filter(is_active=False)  
        # If the active_filter is not present, we can show not active families by default  
        elif active_filter is None:  
            queryset = queryset.filter(is_active=True) 

        # Check family type based on selected option  
        family_type = self.request.GET.get('family_type')  
        if family_type and family_type != 'all':  
            queryset = queryset.filter(family_type=family_type)  

        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries = Family_Type.objects.all()
        family_type_dict = {}
        for query in queries:
            family_type_dict[query.name] = query.id
        print(family_type_dict.items())
        context["family_types"] = family_type_dict
        return context

    

class FamilyCreateView(CreateView):  
    model = Family  
    form_class = NewFamilyForm   
    template_name = 'Family/family_form.html'  
    success_url = reverse_lazy('family_list')  


class FamilyDetailView(View):  
    template_name = 'Family/family_detail.html' 

    def get(self, request, pk):  
        family = get_object_or_404(Family, pk=pk)  
        
        context = {  
            'family': family,  
            'members': family.members.all()  # Access the members directly from the family instance  
        }
        return render(request, self.template_name, context)
    

class FamilyUpdateView(UpdateView):  
    model = Family  
    form_class = FamilyForm    
    template_name = 'Family/family_form.html'  
    success_url = reverse_lazy('family_list')

    def form_valid(self, form):  
        if form.is_valid():  
            return super().form_valid(form)  
        else:  
            print(form.errors)  # Print errors to console or log  
            return self.form_invalid(form)  


class FamilyDeactivateView(View):  
    template_name = 'Family/family_confirm_deactivate.html'  

    def get(self, request, pk):  
        family = get_object_or_404(Family, pk=pk)  
        context = {  
            'family': family  
        }  
        return render(request, self.template_name, context)  

    def post(self, request, pk):  
        family = get_object_or_404(Family, pk=pk)  
        family.is_active = not family.is_active  # Set to inactive  
        family.save()  
        return redirect(reverse_lazy('family_list')) 


#------------ Person views
class PersonListView(View):  
    def get(self, request, family_id):  
        family = get_object_or_404(Family, id=family_id)  
        people = family.people.all()  
        return render(request, 'person/person_list.html', {'family': family, 'people': people})  

class PersonCreateView(View):  
    def get(self, request, family_id):  
        family = get_object_or_404(Family, id=family_id)  
        form = PersonForm(initial={'family': family})  
        return render(request, 'person/person_form.html', {'form': form, 'family': family, 'family_id':family_id})  

    def post(self, request, family_id):  
        family = get_object_or_404(Family, id=family_id)  
        form = PersonForm(request.POST)  
        if form.is_valid():  
            new_person = form.save(commit=False)  
            new_person.family = family  
            new_person.save()  
            return redirect('family_detail', pk=family_id)  
        return render(request, 'person/person_form.html', {'form': form, 'family': family, 'family_id': family_id})  

class PersonUpdateView(View):  
    def get(self, request, family_id, pk):  
        person = get_object_or_404(Person, pk=pk)  
        form = PersonForm(instance=person)  
        return render(request, 'person/person_form.html', {'form': form, 'family_id': family_id, 'person':person})  

    def post(self, request, family_id, pk):  
        person = get_object_or_404(Person, pk=pk)  
        form = PersonForm(request.POST, instance=person)  
        if form.is_valid():  
            form.save()  
            return redirect('family_detail', pk=family_id)  
        return render(request, 'person/person_form.html', {'form': form, 'family_id': family_id})

def set_guardian(request, family_id, pk):
    person = get_object_or_404(Person, pk=pk)
    family = get_object_or_404(Family, id=family_id)
    family.guardian = person
    family.save()
    return redirect('family_detail', pk=family_id)

def active(request, pk):
    family = Family.objects.get(id=pk)
    family.is_active = True
    family.save()
    return redirect("family_list")
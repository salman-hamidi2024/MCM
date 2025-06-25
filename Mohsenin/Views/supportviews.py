from django.views import generic  
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse_lazy 
from ..models import Supporter, Support, Person
from ..forms import SupporterForm  

# List and Create Supporters  
class SupporterListView(generic.ListView):  
    model = Supporter
    context_object_name = 'Supporters'  
    template_name = 'Support/supporter_list.html'  # Create this template  

class SupporterCreateView(generic.CreateView):  
    model = Supporter
    form_class = SupporterForm  
    template_name = 'Support/supporter_form.html'
    success_url = reverse_lazy('supporter-list')  # Create this template  

# List and Create Support for specific Person  
class SupportListView(generic.ListView):  
    model = Support  
    template_name = 'Support/support_list.html'  # Create this template  

    def get_queryset(self):  
        return Support.objects.filter(person=self.kwargs['person_id'])  

class SupportCreateView(generic.CreateView):  
    model = Support  
    template_name = 'Support/support_form.html'  # Create this template  
    fields = ['supporter', 'person', 'amount', 'is_active']

    def form_valid(self, form):  
        # Optionally, you can customize this method  
        return super().form_valid(form)  

# Detail View for a Specific Supporter  
class SupporterDetailView(generic.DetailView):  
    model = Supporter  
    template_name = 'Support/supporter_detail.html'  

    def post(self, request, *args, **kwargs):  
        # If the form for searching by national_id was submitted  
        national_id = request.POST.get('national_id', '').strip()  
        supporter = self.get_object()  

        # Search for the person by national_id  
        searched_person = Person.objects.filter(national_id=national_id).first()  

        # If a person with that national_id is found  
        if searched_person:  
            # If the supporter supports orphans only, check if the found person is an orphan  
            if supporter.supports_orphans_only and not searched_person.is_orphan:  
                # If not an orphan, handle the case accordingly (maybe redirect with an error)  
                return redirect('supporter-detail', pk=supporter.pk)  
            
            # Render detail with the found person  
            return self.render_to_response({'object': supporter, 'searched_person': searched_person})  
        
        # If not found, just return to the same page  
        return self.render_to_response({'object': supporter, 'searched_person': None})
    

class SupporterUpdateView(generic.UpdateView):  
    model = Supporter  
    form_class = SupporterForm    
    template_name = 'Support/Supporter_form.html'  
    success_url = reverse_lazy('supporter-list')

    def form_valid(self, form):  
        if form.is_valid():  
            return super().form_valid(form)  
        else:  
            print(form.errors)  # Print errors to console or log  
            return self.form_invalid(form) 


class SupporterDeactiveView(generic.View):
    template_name = 'Support/supporter_confirm_deactive.html'
    
    def get(self, request, pk):  
        supporter = get_object_or_404(Supporter, pk=pk)  
        context = {  
            'supporter': supporter  
        }  
        return render(request, self.template_name, context)  

    def post(self, request, pk):  
        supporter = get_object_or_404(Supporter, pk=pk)  
        supporter.is_active = not supporter.is_active  # Set to inactive  
        supporter.save()  
        return redirect(reverse_lazy('supporter-list')) 
from django.shortcuts import render, get_object_or_404, redirect  
from django.views import View  
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  
from Mohsenin.models import Family_Type, Family
from Mohsenin.forms import Family_Type_Form



# ----------- family type views
class Family_Type_List_View(ListView):
      template_name = "Family_types/family_type_list.html"
      model = Family_Type
      context_object_name = "family_types"
      
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            family_type_counts = Family_Type.objects.annotate(
            family_count=Count('family')
            ).values('name', 'family_count')
            
            family_types = {item['name']: item['family_count'] for item in family_type_counts}
            print(family_types)
            context['type_count'] = family_types
            return context




class Family_Type_Ceate_View(CreateView):
      model = Family_Type
      form_class = Family_Type_Form
      template_name = "Family_types/family_type_form.html"
      success_url = reverse_lazy("family_type_list")



class Family_Type_Delete_View(DeleteView):
      model = Family_Type
      template_name = "Family_types/family_type_delete.html"
      success_url = reverse_lazy("family_type_list")



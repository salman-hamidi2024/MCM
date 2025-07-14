# from django.shortcuts import render, get_object_or_404, redirect  
# from django.views import View  
# from django.db.models import Count
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy  
# from Mohsenin.models import Family_Type, Family
# from Mohsenin.forms import Family_Type_Form



# # ----------- family type views
# class Family_Type_List_View(ListView):
#       template_name = "Family_types/family_type_list.html"
#       model = Family_Type
#       context_object_name = "family_types"
      
      
#       def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             family_type_counts = Family_Type.objects.annotate(
#             family_count=Count('family')
#             ).values('name', 'family_count')
            
#             family_types = {item['name']: item['family_count'] for item in family_type_counts}
#             print(family_types)
#             context['type_count'] = family_types
#             return context




# class Family_Type_Ceate_View(CreateView):
#       model = Family_Type
#       form_class = Family_Type_Form
#       template_name = "Family_types/family_type_form.html"
#       success_url = reverse_lazy("family_type_list")



# class Family_Type_Delete_View(DeleteView):
#       model = Family_Type
#       template_name = "Family_types/family_type_delete.html"
#       success_url = reverse_lazy("family_type_list")




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count
from Mohsenin.models import Family_Type, Family
from Mohsenin.forms import Family_Type_Form

# List Family Types
def family_type_list(request):
    family_types = Family_Type.objects.all().order_by('name')  # مرتب‌سازی برای خوانایی
    family_type_counts = Family_Type.objects.annotate(
        family_count=Count('family')
    ).values('name', 'family_count')
    
    type_count = {item['name']: item['family_count'] for item in family_type_counts}
    
    context = {
        'family_types': family_types,
        'type_count': type_count,
    }
    return render(request, 'family_types/family_type_list.html', context)

# Create Family Type
def family_type_create(request):
    if request.method == 'POST':
        form = Family_Type_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'نوع خانواده با موفقیت ایجاد شد.')
            return redirect('family_type_list')
        else:
            messages.error(request, 'خطایی در ایجاد نوع خانواده رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = Family_Type_Form()
    
    context = {
        'form': form,
    }
    return render(request, 'family_types/family_type_form.html', context)

# Delete Family Type
def family_type_delete(request, pk):
    family_type = get_object_or_404(Family_Type, pk=pk)
    
    if request.method == 'POST':
        family_type.delete()
        messages.success(request, 'نوع خانواده با موفقیت حذف شد.')
        return redirect('family_type_list')
    
    context = {
        'family_type': family_type,
    }
    return render(request, 'family_types/family_type_delete.html', context)
# from django.shortcuts import render, get_object_or_404, redirect  
# from django.views import View  
# from django.views.generic import ListView, CreateView, UpdateView
# from django.urls import reverse_lazy  
# from ..models import Family, Person, Family_Type
# from ..forms import FamilyForm, NewFamilyForm,PersonForm, SearchForm
# #------------ Family views
# class FamilyListView(ListView):  
#     model = Family  
#     template_name = 'Family/family_list.html'  
#     context_object_name = 'families'

#     def get_queryset(self):  
#         queryset = super().get_queryset()  
#         # Filter by search query  
#         search_query = self.request.GET.get('search_query')  
#         if search_query:
#             queryset = queryset.filter(doc_code__icontains=search_query)  
#         # Filter by active/inactive  
#         active_filter = self.request.GET.get('active_filter')  
#         if active_filter == 'active':  
#             queryset = queryset.filter(is_active=True)  
#         elif active_filter == 'not_active':  
#             queryset = queryset.filter(is_active=False)  
#         # If the active_filter is not present, we can show not active families by default  
#         elif active_filter is None:  
#             queryset = queryset.filter(is_active=True) 

#         # Check family type based on selected option  
#         family_type = self.request.GET.get('family_type')  
#         if family_type and family_type != 'all':  
#             queryset = queryset.filter(family_type=family_type)  

#         return queryset 
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         queries = Family_Type.objects.all()
#         form = SearchForm()
#         context["form"] = form
        
#         family_type_dict = {}
#         for query in queries:
#             family_type_dict[query.name] = query.id
#         print(family_type_dict.items())
#         context["family_types"] = family_type_dict
#         return context

    

# class FamilyCreateView(CreateView):  
#     model = Family  
#     form_class = NewFamilyForm   
#     template_name = 'Family/family_form.html'  
#     success_url = reverse_lazy('family_list')  


# class FamilyDetailView(View):  
#     template_name = 'Family/family_detail.html' 

#     def get(self, request, pk):  
#         family = get_object_or_404(Family, pk=pk)  
        
#         context = {  
#             'family': family,  
#             'members': family.members.all()  # Access the members directly from the family instance  
#         }
#         return render(request, self.template_name, context)
    

# class FamilyUpdateView(UpdateView):  
#     model = Family  
#     form_class = FamilyForm    
#     template_name = 'Family/family_form.html'  
#     success_url = reverse_lazy('family_list')

#     def form_valid(self, form):  
#         if form.is_valid():  
#             return super().form_valid(form)  
#         else:  
#             print(form.errors)  # Print errors to console or log  
#             return self.form_invalid(form)  


# class FamilyDeactivateView(View):  
#     template_name = 'Family/family_confirm_deactivate.html'  

#     def get(self, request, pk):  
#         family = get_object_or_404(Family, pk=pk)  
#         context = {  
#             'family': family  
#         }  
#         return render(request, self.template_name, context)  

#     def post(self, request, pk):  
#         family = get_object_or_404(Family, pk=pk)  
#         family.is_active = not family.is_active  # Set to inactive  
#         family.save()  
#         return redirect(reverse_lazy('family_list')) 


# #------------ Person views
# class PersonListView(View):  
#     def get(self, request, family_id):  
#         family = get_object_or_404(Family, id=family_id)  
#         people = family.people.all()  
#         return render(request, 'person/person_list.html', {'family': family, 'people': people})  

# class PersonCreateView(View):  
#     def get(self, request, family_id):  
#         family = get_object_or_404(Family, id=family_id)  
#         form = PersonForm(initial={'family': family})  
#         return render(request, 'person/person_form.html', {'form': form, 'family': family, 'family_id':family_id})  

#     def post(self, request, family_id):  
#         family = get_object_or_404(Family, id=family_id)  
#         form = PersonForm(request.POST)  
#         if form.is_valid():  
#             new_person = form.save(commit=False)  
#             new_person.family = family  
#             new_person.save()  
            
#             return redirect('family_detail', pk=family_id)  
#         return render(request, 'person/person_form.html', {'form': form, 'family': family, 'family_id': family_id})  

# class PersonUpdateView(View):  
#     def get(self, request, family_id, pk):  
#         person = get_object_or_404(Person, pk=pk)  
#         form = PersonForm(instance=person)  
#         return render(request, 'person/person_form.html', {'form': form, 'family_id': family_id, 'person':person})  

#     def post(self, request, family_id, pk):  
#         person = get_object_or_404(Person, pk=pk)  
#         form = PersonForm(request.POST, instance=person)  
#         if form.is_valid():  
#             form.save()  
#             return redirect('family_detail', pk=family_id)  
#         return render(request, 'person/person_form.html', {'form': form, 'family_id': family_id})

# def set_guardian(request, family_id, pk):
#     person = get_object_or_404(Person, pk=pk)
#     family = get_object_or_404(Family, id=family_id)
#     family.guardian = person
#     family.save()
#     return redirect('family_detail', pk=family_id)

# def active(request, pk):
#     family = Family.objects.get(id=pk)
#     family.is_active = True
#     family.save()
#     return redirect("family_list")





from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from ..models import Family, Person, Family_Type
from ..forms import FamilyForm, NewFamilyForm, PersonForm, SearchForm

# List Families
def family_list(request):
    queryset = Family.objects.all().select_related('family_type')  # بهینه‌سازی کوئری

    # Filter by search query
    search_query = request.GET.get('search_query')
    if search_query:
        queryset = queryset.filter(doc_code__icontains=search_query)

    # Filter by active/inactive
    active_filter = request.GET.get('active_filter')
    if active_filter == 'active':
        queryset = queryset.filter(is_active=True)
    elif active_filter == 'not_active':
        queryset = queryset.filter(is_active=False)
    else:  # Default to active families
        queryset = queryset.all()

    # Filter by family type
    family_type = request.GET.get('family_type')
    if family_type and family_type != 'all':
        queryset = queryset.filter(family_type=family_type)

    # Context data
    family_types = Family_Type.objects.all()
    family_type_dict = {query.name: query.id for query in family_types}
    form = SearchForm()

    context = {
        'families': queryset.order_by('id'),  # مرتب‌سازی برای خوانایی
        'form': form,
        'family_types': family_type_dict,
    }
    return render(request, 'family/family_list.html', context)

# Create Family
def family_create(request):
    if request.method == 'POST':
        form = NewFamilyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'خانواده با موفقیت ساخته شد.')
            return redirect('family_list')
        else:
            messages.error(request, 'خطایی در ایجاد خانواده رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = NewFamilyForm()
    
    context = {
        'form': form,
    }
    return render(request, 'family/family_form.html', context)

# Detail Family
def family_detail(request, pk):
    family = get_object_or_404(Family, pk=pk)
    members = family.members.all().select_related('family')  # بهینه‌سازی کوئری
    context = {
        'family': family,
        'members': members,
    }
    return render(request, 'family/family_detail.html', context)

# Update Family
def family_update(request, pk):
    family = get_object_or_404(Family, pk=pk)
    
    if request.method == 'POST':
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            messages.success(request, 'خانواده با موفقیت به‌روزرسانی شد.')
            return redirect('family_detail', pk)
        else:
            messages.error(request, 'خطایی در به‌روزرسانی خانواده رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = FamilyForm(instance=family)
    
    context = {
        'form': form,
        'family': family,
    }
    return render(request, 'family/family_form.html', context)

# Deactivate/Activate Family
def family_deactivate(request, pk):
    family = get_object_or_404(Family, pk=pk)
    
    if request.method == 'POST':
        family.is_active = not family.is_active
        family.save()
        status = 'فعال' if family.is_active else 'غیرفعال'
        messages.success(request, f'خانواده با موفقیت {status} شد.')
        return redirect('family_list')
    
    context = {
        'family': family,
    }
    return render(request, 'family/family_confirm_deactivate.html', context)

# List People in a Family
def person_list(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    people = family.people.all().select_related('family')  # بهینه‌سازی کوئری
    context = {
        'family': family,
        'people': people,
    }
    return render(request, 'person/person_list.html', context)

# Create Person
def person_create(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    # کد ملی تکراری
    national_id = request.POST.get('national_id')
    if Person.objects.filter(national_id=national_id, family=family).exists():
        messages.warning(request, 'کد ملی تکراری است.')
        return redirect('family_detail', pk=family_id)

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new_person = form.save(commit=False)
            new_person.family = family
            
            new_person.save()
            messages.success(request, 'شخص با موفقیت به خانواده اضافه شد.')
            return redirect('family_detail', pk=family_id)
        else:
            messages.error(request, 'خطایی در افزودن شخص رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PersonForm(initial={'family': family})
    
    context = {
        'form': form,
        'family': family,
        'family_id': family_id,
    }
    return render(request, 'person/person_form.html', context)

# Update Person
def person_update(request, family_id, pk):
    person = get_object_or_404(Person, pk=pk, family_id=family_id)
    
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'شخص با موفقیت به‌روزرسانی شد.')
            return redirect('family_detail', pk=family_id)
        else:
            messages.error(request, 'خطایی در به‌روزرسانی شخص رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PersonForm(instance=person)
    
    context = {
        'form': form,
        'family_id': family_id,
        'person': person,
    }
    return render(request, 'person/person_form.html', context)

# Set Guardian for Family
def set_guardian(request, family_id, pk):
    person = get_object_or_404(Person, pk=pk, family_id=family_id)
    family = get_object_or_404(Family, id=family_id)
    request.method = "POST"
    if request.method == 'POST':
        family.guardian = person
        family.save()
        messages.success(request, 'سرپرست خانواده با موفقیت تنظیم شد.')
        return redirect('family_detail', pk=family_id)
    
    # در صورت درخواست GET، به صفحه جزئیات خانواده هدایت شود
    messages.error(request, 'درخواست نامعتبر است.')
    return redirect('family_detail', pk=family_id)

# Activate Family
def family_activate(request, pk):
    family = get_object_or_404(Family, id=pk)
    
    if request.method == 'POST':
        family.is_active = True
        family.save()
        messages.success(request, 'خانواده با موفقیت فعال شد.')
        return redirect('family_list')
    
    # در صورت درخواست GET، به صفحه لیست خانواده‌ها هدایت شود
    messages.error(request, 'درخواست نامعتبر است.')
    return redirect('family_list')
# from django.views import generic  
# from django.shortcuts import get_object_or_404, redirect
# from django.shortcuts import render
# from django.urls import reverse_lazy 
# from ..models import Supporter, Support, Person
# from ..forms import SupporterForm  
# from django.http import HttpResponseBadRequest

# # List and Create Supporters  
# class SupporterListView(generic.ListView):  
#     model = Supporter
#     context_object_name = 'Supporters'  
#     template_name = 'Support/supporter_list.html'  # Create this template  

# class SupporterCreateView(generic.CreateView):  
#     model = Supporter
#     form_class = SupporterForm  
#     template_name = 'Support/supporter_form.html'
#     success_url = reverse_lazy('supporter-list')  # Create this template  

# # List and Create Support for specific Person  
# class SupportListView(generic.ListView):  
#     model = Support  
#     template_name = 'Support/support_list.html'  # Create this template  

#     def get_queryset(self):  
#         return Support.objects.filter(person=self.kwargs['person_id'])  

# class SupportCreateView(generic.CreateView):  
#     model = Support  
#     template_name = 'Support/support_form.html'  # Create this template  
#     fields = ['supporter', 'person', 'amount', 'is_active']

#     def form_valid(self, form):  
#         # Optionally, you can customize this method  
#         return super().form_valid(form) 

# # Detail View for a Specific Supporter  
# class SupporterDetailView(generic.DetailView):  
#     model = Supporter  
#     template_name = 'Support/supporter_detail.html'  

#     def post(self, request, *args, **kwargs):  
#         # If the form for searching by national_id was submitted  
#         national_id = request.POST.get('national_id', '').strip()  
#         supporter = self.get_object()  

#         # Search for the person by national_id  
#         searched_person = Person.objects.filter(national_id__icontains=national_id).first()  

#         # If a person with that national_id is found  
#         if searched_person:  
#             # If the supporter supports orphans only, check if the found person is an orphan  
#             if supporter.supports_orphans_only and not searched_person.is_orphan:  
#                 # If not an orphan, handle the case accordingly (maybe redirect with an error)  
#                 return redirect('supporter-detail', pk=supporter.pk)  
            
#             # Render detail with the found person  
#             return self.render_to_response({'object': supporter, 'searched_person': searched_person})  
        
#         # If not found, just return to the same page  
#         return self.render_to_response({'object': supporter, 'searched_person': None})
    

# class SupporterUpdateView(generic.UpdateView):  
#     model = Supporter  
#     form_class = SupporterForm    
#     template_name = 'Support/Supporter_form.html'  
#     success_url = reverse_lazy('supporter-list')

#     def form_valid(self, form):  
#         if form.is_valid():  
#             return super().form_valid(form)  
#         else:  
#             print(form.errors)  # Print errors to console or log  
#             return self.form_invalid(form) 


# class SupporterDeactiveView(generic.View):
#     template_name = 'Support/supporter_confirm_deactive.html'
    
#     def get(self, request, pk):  
#         supporter = get_object_or_404(Supporter, pk=pk)  
#         context = {  
#             'supporter': supporter  
#         }  
#         return render(request, self.template_name, context)  

#     def post(self, request, pk):  
#         supporter = get_object_or_404(Supporter, pk=pk)  
#         supporter.is_active = not supporter.is_active  # Set to inactive  
#         supporter.save()  
#         return redirect(reverse_lazy('supporter-list')) 

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from ..models import Supporter, Support, Person
from ..forms import SupporterForm
from django.http import HttpResponseBadRequest

# List Supporters
def supporter_list(request):
    supporters = Supporter.objects.filter(is_active=True).order_by('name')  # فقط حامیان فعال
    context = {
        'supporters': supporters,
    }
    return render(request, 'support/supporter_list.html', context)

# Create Supporter
def supporter_create(request):
    if request.method == 'POST':
        form = SupporterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'حامی با موفقیت ایجاد شد.')
            return redirect('supporter-list')
        else:
            messages.error(request, 'خطایی در ایجاد حامی رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = SupporterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'support/supporter_form.html', context)

# List Support for a Specific Person
def support_list(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    supports = Support.objects.all()
    context = {
        'supports': supports,
        'person': person,
    }
    return render(request, 'support/supporter_list.html', context)

# Create Support
def support_create(request, person_id=None):
    person = get_object_or_404(Person, pk=person_id) if person_id else None
    
    if request.method == 'POST':
        # ایجاد فرم با داده‌های ارسالی
        form = SupporterForm(request.POST)
        if form.is_valid():
            support = form.save(commit=False)
            if person:
                support.person = person
            if support.amount <= 0:
                messages.error(request, 'مقدار حمایت باید مثبت باشد.')
                return render(request, 'support/support_form.html', {'form': form})
            support.save()
            messages.success(request, 'حمایت با موفقیت ثبت شد.')
            return redirect('supporter-list')  # یا به صفحه لیست حمایت‌ها هدایت کنید
        else:
            messages.error(request, 'خطایی در ثبت حمایت رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        # مقدار اولیه برای فرم
        initial = {'person': person} if person else {}
        form = SupporterForm(initial=initial)
    
    context = {
        'form': form,
        'person': person,
    }
    return render(request, 'support/support_form.html', context)

# Detail View for a Specific Supporter
def supporter_detail(request, pk):
    supporter = get_object_or_404(Supporter, pk=pk)
    supports = Support.objects.all()
    
    searched_person = None
    if request.method == 'POST':
        national_id = request.POST.get('national_id', '').strip()
        if not national_id:
            messages.error(request, 'لطفاً کد ملی را وارد کنید.')
        else:
            searched_person = Person.objects.filter(national_id__iexact=national_id).first()
            if not searched_person:
                messages.error(request, 'شخصی با این کد ملی یافت نشد.')
            elif supporter.supports_orphans_only and not searched_person.is_orphan:
                messages.error(request, 'این حامی فقط از یتیمان حمایت می‌کند.')
                searched_person = None  # برای جلوگیری از نمایش شخص غیرمجاز
            else:
                messages.success(request, 'شخص با موفقیت پیدا شد.')

    context = {
        'supporter': supporter,
        'supports': supports,
        'searched_person': searched_person,
    }
    return render(request, 'support/supporter_detail.html', context)

# Update Supporter
def supporter_update(request, pk):
    supporter = get_object_or_404(Supporter, pk=pk)
    
    if request.method == 'POST':
        form = SupporterForm(request.POST, instance=supporter)
        if form.is_valid():
            form.save()
            messages.success(request, 'حامی با موفقیت به‌روزرسانی شد.')
            return redirect('supporter-list')
        else:
            messages.error(request, 'خطایی در به‌روزرسانی حامی رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = SupporterForm(instance=supporter)
    
    context = {
        'form': form,
        'supporter': supporter,
    }
    return render(request, 'support/supporter_form.html', context)

# Deactivate/Activate Supporter
def supporter_deactivate(request, pk):
    supporter = get_object_or_404(Supporter, pk=pk)
    
    if request.method == 'POST':
        supporter.is_active = not supporter.is_active
        supporter.save()
        status = 'فعال' if supporter.is_active else 'غیرفعال'
        messages.success(request, f'حامی با موفقیت {status} شد.')
        return redirect('supporter-list')
    
    context = {
        'supporter': supporter,
    }
    return render(request, 'support/supporter_confirm_deactivate.html', context)
# from django.shortcuts import render, get_object_or_404, redirect  
# from django.views import View  
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView  
# from django.urls import reverse_lazy  
# from .. models import Family, Dist
# from .. forms import DistForm



# #-------------- Distribution list views
# class DistListView(ListView):
#     model = Dist
#     template_name = 'Dist/Dist_list.html'
#     context_object_name = 'dists'

#     def get_context_data(self, **kwargs):  
#         context = super().get_context_data(**kwargs)  
#         return context


# class DistCreateView(CreateView):
#     model = Dist
#     form_class = DistForm
#     template_name = 'Dist/Dist_form.html'
#     success_url = reverse_lazy('dist_list')


# class DistDetailView(View):
#     template_name = 'Dist/dist_detail.html'

#     def get(self, request, pk):
#         dist = get_object_or_404(Dist, pk=pk)  
#         families = dist.families.all() 
#         context = {  
#         'dist': dist,  
#         'families': families,  
#         }  
#         return render(request, self.template_name, context)

# class DistUpdateView(UpdateView):  
#     model = Dist  
#     form_class = DistForm  # Use a ModelForm for Family  
#     template_name = 'Dist/Dist_form.html'  
#     success_url = reverse_lazy('dist_list')

# class DistDeleteView(View):  
#     def get(self, request, pk):  
#         dist = get_object_or_404(Dist, pk=pk)  
#         return render(request, 'Dist/dist_confirm_delete.html', {'dist': dist})  
    
#     def post(self, request, pk):  
#         dist = get_object_or_404(Dist, pk=pk)  
#         dist.delete()  
#         return redirect(reverse_lazy('dist_list'))
    


# def FamiliesWithoutDist(request, pk):
#     families = Family.objects.filter(distlist__isnull=True)
#     dist = get_object_or_404(Dist, pk=pk)  
#     return render(request, 'Dist/dist_select_families.html', {'families': families, 'dist':dist}) 


# def associate_family_to_dist(request, pk):  
#     if request.method == "POST":  
#         family_ids = request.POST.getlist('family_ids') 
#         dist = get_object_or_404(Dist, id=pk)
#         Family.objects.filter(id__in=family_ids).update(distlist=dist)  
#         return redirect('dist_detail', pk=pk)


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse_lazy
from ..models import Family, Dist
from ..forms import DistForm

# List Distributions
def dist_list(request):
    dists = Dist.objects.all().order_by('id')  # مرتب‌سازی برای خوانایی
    context = {
        'dists': dists,
    }
    return render(request, 'dist/dist_list.html', context)

# Create Distribution
def dist_create(request):
    if request.method == 'POST':
        form = DistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'توزیع با موفقیت ایجاد شد.')
            return redirect('dist_list')
        else:
            messages.error(request, 'خطایی در ایجاد توزیع رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = DistForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dist/dist_form.html', context)

# Detail Distribution
def dist_detail(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    families = dist.families.all().order_by('family_type').select_related('distlist')  # بهینه‌سازی کوئری
    context = {
        'dist': dist,
        'families': families,
    }
    return render(request, 'dist/dist_detail.html', context)

# Update Distribution
def dist_update(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    
    if request.method == 'POST':
        form = DistForm(request.POST, instance=dist)
        if form.is_valid():
            form.save()
            messages.success(request, 'توزیع با موفقیت به‌روزرسانی شد.')
            return redirect('dist_list')
        else:
            messages.error(request, 'خطایی در به‌روزرسانی توزیع رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = DistForm(instance=dist)
    
    context = {
        'form': form,
        'dist': dist,
    }
    return render(request, 'dist/dist_form.html', context)

# Delete Distribution
def dist_delete(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    
    if request.method == 'POST':
        dist.delete()
        messages.success(request, 'توزیع با موفقیت حذف شد.')
        return redirect('dist_list')
    
    context = {
        'dist': dist,
    }
    return render(request, 'dist/dist_confirm_delete.html', context)

# List Families Without Distribution
def families_without_dist(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    families = Family.objects.filter(distlist__isnull=True).order_by('id')  # خانواده‌های بدون توزیع
    context = {
        'families': families,
        'dist': dist,
    }
    return render(request, 'dist/dist_select_families.html', context)

# Associate Families to Distribution
def associate_family_to_dist(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    
    if request.method == 'POST':
        family_ids = request.POST.getlist('family_ids')
        if not family_ids:
            messages.error(request, 'هیچ خانواده‌ای انتخاب نشده است.')
            return redirect('families_without_dist', pk=pk)
        
        # به‌روزرسانی خانواده‌های انتخاب‌شده
        updated_count = Family.objects.filter(id__in=family_ids).update(distlist=dist)
        if updated_count:
            messages.success(request, f'{updated_count} خانواده با موفقیت به توزیع اضافه شد.')
        else:
            messages.error(request, 'خطایی در افزودن خانواده‌ها رخ داد.')
        
        return redirect('dist_detail', pk=pk)
    
    # در صورت درخواست GET، به صفحه انتخاب خانواده‌ها هدایت شود
    return redirect('families_without_dist', pk=pk)



def remove_family_from_dist(request, dist_pk, family_pk):
    family = get_object_or_404(Family, pk=family_pk)
    family.distlist = None
    family.save()
    messages.success(request, 'خانواده با موفقیت از توزیع حذف شد.')
    return redirect('dist_detail', pk=dist_pk)


def list_dist_for_transfer(request, dist_pk, family_pk):
    family = get_object_or_404(Family, pk=family_pk)
    dist = get_object_or_404(Dist, pk=dist_pk)
    members = family.members.all()  # بهینه‌سازی کوئری
    all_dists = Dist.objects.exclude(pk=dist_pk)

    context = {
        'family': family,
        'dist': dist,
        'members': members,
        'all_dists': all_dists,
    }
    return render(request, 'dist/transfer_dist_list.html', context)



def transfer_family_to_dist(request, dist_pk, family_pk):
    try:
        family = get_object_or_404(Family, pk=family_pk)
        dist = get_object_or_404(Dist, pk=dist_pk)

        family.distlist = dist
        family.save()
        messages.success(request, 'خانواده با موفقیت به توزیع منتقل شد.')
        print(f'خانواده {family.pk} به توزیع {dist.pk} منتقل شد.')
        return redirect('dist_detail', pk=dist_pk)
    except Exception as e:
        print(f'خطا در انتقال خانواده به توزیع: {str(e)}')
        messages.error(request, f'خطا در انتقال خانواده به توزیع: {str(e)}')
        return redirect('dist_detail', pk=dist_pk)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Family, Dist, Person
from .forms import FamilyForm, NewFamilyForm, DistForm, PersonForm

# Index View
def index(request):
    return render(request, 'mohsenin/index.html')

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

# List Observations for a Family
def observation_list(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    observations = family.observation_set.all().order_by('-id')  # مرتب‌سازی برای نمایش جدیدترین‌ها
    context = {
        'family': family,
        'observations': observations,
    }
    return render(request, 'observations/observation_list.html', context)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from ..models import Package, PackageDistribution
from ..forms import PackageForm, PackageDistributionForm

# List Packages
def package_list(request):
    packages = Package.objects.all().order_by('id')  # مرتب‌سازی برای خوانایی
    context = {
        'packages': packages,
    }
    return render(request, 'package/package_list.html', context)

# Create Package
def package_create(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'بسته با موفقیت ایجاد شد.')
            return redirect('packages_list')
        else:
            messages.error(request, 'خطایی در ایجاد بسته رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PackageForm()
    
    context = {
        'form': form,
    }
    return render(request, 'package/packages_form.html', context)

# Update Package
def package_update(request, pk):
    package = get_object_or_404(Package, pk=pk)
    
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'بسته با موفقیت به‌روزرسانی شد.')
            return redirect('packages_list')
        else:
            messages.error(request, 'خطایی در به‌روزرسانی بسته رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PackageForm(instance=package)
    
    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'package/packages_form.html', context)

# Delete Package
def package_delete(request, pk):
    package = get_object_or_404(Package, pk=pk)
    
    if request.method == 'POST':
        package.delete()
        messages.success(request, 'بسته با موفقیت حذف شد.')
        return redirect('packages_list')
    
    context = {
        'package': package,
    }
    return render(request, 'package/packages_confirm_delete.html', context)

# Detail Package
def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package_distributions = PackageDistribution.objects.filter(package=package).select_related('package')
    context = {
        'package': package,
        'packages': package_distributions,  # نام متغیر مطابق با CBV اصلی
    }
    return render(request, 'package/package_detail.html', context)

# Create Package Distribution
def package_distribution_create(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    
    if request.method == 'POST':
        form = PackageDistributionForm(request.POST)
        if form.is_valid():
            package_distribution = form.save(commit=False)
            package_distribution.package = package
            package_distribution.save()
            messages.success(request, 'توزیع بسته با موفقیت ثبت شد.')
            return redirect('packages_list')
        else:
            messages.error(request, 'خطایی در ثبت توزیع بسته رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PackageDistributionForm()
    
    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'package/package_distribution/package_distribution_form.html', context)

# Update Package Distribution
def package_distribution_update(request, package_id, pk):
    package = get_object_or_404(Package, pk=package_id)
    package_distribution = get_object_or_404(PackageDistribution, pk=pk, package=package)
    
    if request.method == 'POST':
        form = PackageDistributionForm(request.POST, instance=package_distribution)
        if form.is_valid():
            form.save()
            messages.success(request, 'توزیع بسته با موفقیت به‌روزرسانی شد.')
            return redirect('package_detail', pk=package.id)
        else:
            messages.error(request, 'خطایی در به‌روزرسانی توزیع بسته رخ داد. لطفاً فرم را بررسی کنید.')
    else:
        form = PackageDistributionForm(instance=package_distribution)
    
    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'package/package_distribution/package_distribution_form.html', context)

# Delete Package Distribution
def package_distribution_delete(request, package_id, pk):
    package_distribution = get_object_or_404(PackageDistribution, pk=pk, package__id=package_id)
    
    if request.method == 'POST':
        package_distribution.delete()
        messages.success(request, 'توزیع بسته با موفقیت حذف شد.')
        return redirect('package_detail', pk=package_id)
    
    context = {
        'package_distribution': package_distribution,
        'package': package_distribution.package,
    }
    return render(request, 'package/package_distribution/package_distribution_confirm_delete.html', context)
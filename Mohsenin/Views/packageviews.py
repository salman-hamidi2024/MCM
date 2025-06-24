from django.shortcuts import render, get_object_or_404, redirect  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView  
from django.urls import reverse_lazy
from .. models import Package
from .. forms import PackageDistributionForm, PackageForm



#-------------- Packages views
class PackageListView(ListView):
    template_name = "Package/package_list.html"
    model = Package
    context_object_name = "packages"


# def package_list(request):
#     return convert_xml(Package)


class PackageCreateView(CreateView):
    template_name = "Package/packages_form.html"
    model = Package
    form_class = PackageForm
    success_url = reverse_lazy("packages_list")


class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    success_url = reverse_lazy('packages_list')
    template_name = "Package/packages_form.html"


class PackageDeleteView(DeleteView):
    model = Package
    success_url = reverse_lazy("packages_list")
    template_name = "Package/packages_confirm_delete.html"


class PackageDetailView(DetailView):
    model = Package
    template_name = "Package/package_detail.html"
    context_object_name = "package"
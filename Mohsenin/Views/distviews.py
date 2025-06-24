from django.shortcuts import render, get_object_or_404, redirect  
from django.views import View  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  
from django.urls import reverse_lazy  
from .. models import Family, Dist
from .. forms import DistForm



#-------------- Distribution list views
class DistListView(ListView):
    model = Dist
    template_name = 'Dist/Dist_list.html'
    context_object_name = 'dists'

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        return context


class DistCreateView(CreateView):
    model = Dist
    form_class = DistForm
    template_name = 'Dist/Dist_form.html'
    success_url = reverse_lazy('dist_list')


class DistDetailView(View):
    template_name = 'Dist/dist_detail.html'

    def get(self, request, pk):
        dist = get_object_or_404(Dist, pk=pk)  
        families = dist.families.all() 
        context = {  
        'dist': dist,  
        'families': families,  
        }  
        return render(request, self.template_name, context)

class DistUpdateView(UpdateView):  
    model = Dist  
    form_class = DistForm  # Use a ModelForm for Family  
    template_name = 'Dist/Dist_form.html'  
    success_url = reverse_lazy('dist_list')

class DistDeleteView(View):  
    def get(self, request, pk):  
        dist = get_object_or_404(Dist, pk=pk)  
        return render(request, 'Dist/dist_confirm_delete.html', {'dist': dist})  
    
    def post(self, request, pk):  
        dist = get_object_or_404(Dist, pk=pk)  
        dist.delete()  
        return redirect(reverse_lazy('dist_list'))
    


def FamiliesWithoutDist(request, pk):
    families = Family.objects.filter(distlist__isnull=True)
    dist = get_object_or_404(Dist, pk=pk)  
    return render(request, 'Dist/dist_select_families.html', {'families': families, 'dist':dist}) 


def associate_family_to_dist(request, pk):  
    if request.method == "POST":  
        family_ids = request.POST.getlist('family_ids') 
        dist = get_object_or_404(Dist, id=pk)
        Family.objects.filter(id__in=family_ids).update(distlist=dist)  
        return redirect('dist_detail', pk=pk)
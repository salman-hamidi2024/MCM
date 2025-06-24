from django import forms  
from .models import Family, Dist, Person, Package, PackageDistribution, Supporter

class DistForm(forms.ModelForm):
    class Meta:
        model = Dist
        fields = '__all__'

class FamilyForm(forms.ModelForm):  
    class Meta:  
        model = Family  
        fields = ['doc_code', 'need_level', 'family_type', 'address', 'contact_number', 'postal_code',  'is_active', 'distlist'] 

class NewFamilyForm(forms.ModelForm):  
    class Meta:  
        model = Family  
        fields = ['doc_code', 'need_level', 'family_type', 'address', 'contact_number', 'postal_code',  'is_active']

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person 
        fields = '__all__'


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"

class PackageDistributionForm(forms.ModelForm):
    class Meta:
        model = PackageDistribution
        fields = "__all__"

class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = "__all__"
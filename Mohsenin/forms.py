from django import forms  
from .models import Family, Dist, Person, Package, PackageDistribution, Supporter, Family_Type

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
        fields = ["family","members","distribution_date","is_active"]

class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = "__all__"



class Family_Type_Form(forms.ModelForm):
    class Meta:
        model = Family_Type
        fields = ["name"]


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder':  'جستجوی خانواده...'}))

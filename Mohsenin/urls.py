from django.urls import path
from . import views
from . Views import familyviews
from . Views import distviews
from . Views import packageviews
from . Views import family_type
from . Views import supportviews #only for people support childs monthly (cash)
urlpatterns = [
    #path(<'addres':str>, <function>, <name='name':str>)
    path('', views.index, name="index"),

    #------Dist, FYI Distributions
    path('dists/', distviews.DistListView.as_view(), name='dist_list'),
    path('dist/create/', distviews.DistCreateView.as_view(), name='dist_create'),
    path('dist/<int:pk>/update', distviews.DistUpdateView.as_view(), name='dist_update'),
    path('dist/<int:pk>/delete/', distviews.DistDeleteView.as_view(), name='dist_delete'),
    path('dist/<int:pk>/', distviews.DistDetailView.as_view(), name='dist_detail'),
    path('dist/select/<int:pk>/', distviews.FamiliesWithoutDist, name='families_without_dist'),  
    path('dist/assosiate/<int:pk>/', distviews.associate_family_to_dist, name='associate_family_to_dist'),

    #----- Family
    path('families/', familyviews.FamilyListView.as_view(), name='family_list'),  
    path('families/create/', familyviews.FamilyCreateView.as_view(), name='family_create'),  
    path('families/<int:pk>/', familyviews.FamilyDetailView.as_view(), name='family_detail'),  
    path('families/<int:pk>/update/', familyviews.FamilyUpdateView.as_view(), name='family_update'),  
    path('families/<int:pk>/deactivate/', familyviews.FamilyDeactivateView.as_view(), name='family_deactivate'),

    #------ Person
    #path('families/<int:family_id>/members/', views.PersonListView.as_view(), name='person_list'),  
    path('families/<int:family_id>/members/add/', familyviews.PersonCreateView.as_view(), name='person_create'),
    path('families/<int:family_id>/members/<int:pk>/guardian/', familyviews.set_guardian, name='person_as_guardian'),  
    path('families/<int:family_id>/members/<int:pk>/edit/', familyviews.PersonUpdateView.as_view(), name='person_update'),  

    path('families/<int:family_id>/observations/', views.ObservationListView.as_view(), name='observation_list'),

        #----- Packages
    path("packages/", packageviews.PackageListView.as_view(), name="packages_list"),
    path("packages/add/", packageviews.PackageCreateView.as_view(), name="package_create"),
    path("packages/<int:pk>/update/", packageviews.PackageUpdateView.as_view(), name="package_update"),
    path("packages/<int:pk>/delete/", packageviews.PackageDeleteView.as_view(), name="package_delete"),
    path("packages/<int:pk>/", packageviews.PackageDetailView.as_view(), name="package_detail"),
    #path("packages_convert_xml", packageviews.package_list, name="download_package"),


    path('supporters/', supportviews.SupporterListView.as_view(), name='supporter-list'),  
    path('supporters/add/', supportviews.SupporterCreateView.as_view(), name='supporter-create'),
    path('supporter/<int:pk>/', supportviews.SupporterDetailView.as_view(), name='supporter-detail'),
    path('supporter/<int:pk>/update/', supportviews.SupporterUpdateView.as_view(), name='supporter-update'),
    path('support/<int:person_id>/', supportviews.SupportListView.as_view(), name='support-list'),  
    path('supporter/<int:pk>/deactive', supportviews.SupporterDeactiveView.as_view(), name="support-deactive"),
    path('support/new/', supportviews.SupportCreateView.as_view(), name='support-create'),  


    #------- family type
    path("family_type_list", family_type.Family_Type_List_View.as_view(), name="family_type_list"),
    path("family_type_create", family_type.Family_Type_Ceate_View.as_view(), name="family_type_create"),
    path("family_type_delete/<int:pk>", family_type.Family_Type_Delete_View.as_view(), name="family_type_delete"),
    
    
]
 
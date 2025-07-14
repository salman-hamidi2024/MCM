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
    path('dists/', distviews.dist_list, name='dist_list'),
    path('dist/create/', distviews.dist_create, name='dist_create'),
    path('dist/<int:pk>/update', distviews.dist_update, name='dist_update'),
    path('dist/<int:pk>/delete/', distviews.dist_delete, name='dist_delete'),
    path('dist/<int:pk>/', distviews.dist_detail, name='dist_detail'),
    path('dist/select/<int:pk>/', distviews.families_without_dist, name='families_without_dist'),  
    path('dist/assosiate/<int:pk>/', distviews.associate_family_to_dist, name='associate_family_to_dist'),
    path('dist/remove_family/<int:dist_pk>/<int:family_pk>/', distviews.remove_family_from_dist, name='remove_family_from_dist'),
    path('dist/transfer/list/<int:dist_pk>/<int:family_pk>/', distviews.list_dist_for_transfer, name='list_dist_for_transfer'),
    path('dist/transfer/<int:dist_pk>/<int:family_pk>/', distviews.transfer_family_to_dist, name='transfer_family_to_dist'),

    #----- Family
    path('families/', familyviews.family_list, name='family_list'),  
    path('families/create/', familyviews.family_create, name='family_create'),  
    path('families/<int:pk>/', familyviews.family_detail, name='family_detail'),  
    path('families/<int:pk>/update/', familyviews.family_update, name='family_update'),  
    path('families/<int:pk>/deactivate/', familyviews.family_deactivate, name='family_deactivate'),
    path('families/<int:pk>/active/', familyviews.family_activate, name="active_family"),

    #------ Person
    #path('families/<int:family_id>/members/', views.PersonListView, name='person_list'),  
    path('families/<int:family_id>/members/add/', familyviews.person_create, name='person_create'),
    path('families/<int:family_id>/members/<int:pk>/guardian/', familyviews.set_guardian, name='person_as_guardian'),  
    path('families/<int:family_id>/members/<int:pk>/edit/', familyviews.person_update, name='person_update'),  

    path('families/<int:family_id>/observations/', views.observation_list, name='observation_list'),

        #----- Packages
    path("packages/", packageviews.package_list, name="packages_list"),
    path("packages/add/", packageviews.package_create, name="package_create"),
    path("packages/<int:pk>/update/", packageviews.package_update, name="package_update"),
    path("packages/<int:pk>/delete/", packageviews.package_delete, name="package_delete"),
    path("packages/<int:pk>/", packageviews.package_detail, name="package_detail"),
    #path("packages_convert_xml", packageviews.package_list, name="download_package"),
    
    #------- package distribution
    path("packagedistribution/<int:package_id>/create", packageviews.package_distribution_create, name="packagedistributioncreate"),
    path("packagedistribution/<int:package_id>/update/<int:pk>/", packageviews.package_distribution_update, name="packagedistributionupdate"),
    path("packagedistribution/<int:package_id>/delete/<int:pk>/", packageviews.package_distribution_delete, name="packagedistributiondelete"),
    # path("packagedistribution/<int:family_id>/list-transfer", packageviews.package_distribution_list_transfer, name="packagedistributionlisttransfer"),
    # path("packagedistribution/<int:package_id>/transfer/<int:family_id>/", packageviews.transfer_package_distribution, name="packagedistributiontransfer"),



    path('supporters/', supportviews.supporter_list, name='supporter-list'),  
    path('supporters/add/', supportviews.supporter_create, name='supporter-create'),
    path('supporter/<int:pk>/', supportviews.supporter_detail, name='supporter-detail'),
    path('supporter/<int:pk>/update/', supportviews.supporter_update, name='supporter-update'),
    path('support/<int:person_id>/', supportviews.support_list, name='support-list'),  
    path('supporter/<int:pk>/deactivate', supportviews.supporter_deactivate, name="support-deactivate"),
    path('support/new/', supportviews.support_create, name='support-create'),  


    #------- family type
    path("family_type_list", family_type.family_type_list, name="family_type_list"),
    path("family_type_create", family_type.family_type_create, name="family_type_create"),
    path("family_type_delete/<int:pk>", family_type.family_type_delete, name="family_type_delete"),


]
 
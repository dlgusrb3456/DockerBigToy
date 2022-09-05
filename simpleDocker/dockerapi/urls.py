from django.urls import path

from . import views

urlpatterns = [
    path('makenetwork/',views.makeNetwork),
    path('networklist/',views.network_list), 
    path('networkinspect/<networkname>',views.network_inspect), 
    path('networkdelete/<networkname>',views.network_delete), 
    path('stackmake/',views.create), 
    path('logout',views.logout_docker),
    path('rmstack/<stackname>',views.rmstack),
    path('psstack/<stackname>',views.psstack),
    path('servicelist',views.service_list),
    path('servicescale/<servicename>',views.servicescale),
    path('serviceupdate/<servicename>',views.serviceupdate),
    path('servicerollback/<servicename>',views.servicerollback),
    path('volumemake/',views.makevolume), 
    path('volumelist/',views.listvolume), 
    path('volumeinspect/<volumename>',views.volume_inspect), 
    path('volumedelete/<volumename>',views.volume_delete), 
    path('main',views.main), 
    
    path('imagelist/',views.image_list), 
    path('imagemake/',views.create_image), 
    path('rmimage/<imagename>/<imagetag>',views.image_remove), 
    path('imagepull',views.image_pull), 
    path('imagepush',views.image_push),
    path('',views.login_docker), 
]

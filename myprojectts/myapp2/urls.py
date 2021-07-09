from django.urls import path
from .import views

urlpatterns=[

    path('',views.studentForm,name='studentForm'),
    path('addData', views.addData, name='addData'),
    path('show', views.showData, name='show'),
    path('loadform',views.loadModelForm,name='loadForm'),



]
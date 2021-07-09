from django.urls import path
from .import views
#list of urls
urlpatterns=[
    #urlname  #function name  #used while linking pages
    path('',views.home_function,name='homepage'),  # '' means default page
    path('aboutus',views.about_function,name="aboutpage"),


]
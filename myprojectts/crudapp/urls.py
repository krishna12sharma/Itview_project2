from django.urls import path
from .import views
urlpatterns=[

    path('',views.loadForm),
    path('insertEmployee',views.insertEmployee,name='insertEmployee'),
    path('showEmployee',views.showEmployee,name='showEmployee'),
    path('delete/<int:eid>',views.deleteEmployee,name='deleteEmployee'),#pass paramter in urls
    path('updateEmployee/<int:eid>',views.updateEmployee,name='updateEmployee')




]


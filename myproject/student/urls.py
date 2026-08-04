from django.urls import path
from . import views



urlpatterns =[
   path ('',views.home, name='home'),
   path('contact',views.contact,name='contact'),
   path('about',views.about,name='about'),
   path('list',views.list,name='list'),
   path('add',views.add,name='add'),
   path('edit/<int:id>',views.edit,name='edit'),
   path('delete/<int:id>',views.delete,name='delete'),



]


from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.index,name="home" ),
    path('contact', views.contact,name="contact" ),
    path('about', views.about,name="about" ),
    path('session',views.session,name="session"),
    path('department',views.department,name="department"),
    path('doctors',views.doctors,name="doctors"),
    path('products',views.products,name="products"),
    path('crud',views.crud,name='crud'),
    path('crud_add',views.crud_add,name="crud_add"),
    path('addrec',views.addrec,name='addrec'),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name='update'),
    path('update/uprec/<int:id>',views.uprec,name='uprec'),
]
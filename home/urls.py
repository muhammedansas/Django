from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.index,name="home" ),
    path('contact', views.contact,name="contact" ),
    path('about', views.about,name="about" ),
    path('session',views.session,name="session"),
    path('department',views.department,name="department"),
    path('doctors',views.doctors,name="doctors"),
    path('products',views.products,name="products")
]
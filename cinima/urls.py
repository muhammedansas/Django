from django.urls import path,include
from . import views

urlpatterns = [
    path('m_home',views.home,name='m_home'),
    path('m_signup',views.signup,name='m_signup'),
    path('m_login',views.login,name='m_login'),
    path('m_add',views.add,name='m_add'),
    path('m_adding',views.adding,name='m_adding'),
    path('m_delete/<int:id>',views.delete,name='m_delete'),
    path('m_update/<int:id>',views.update,name='m_update'),
]

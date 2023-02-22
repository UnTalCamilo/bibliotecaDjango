from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('', views.InicioView.as_view(), name='inicio'),
    path('', login_required(views.InicioView.as_view()), name='inicio'),
    #path('home/', views.InicioView.as_view(), name='home'),
    path('home/', login_required(views.InicioView.as_view()), name='home'),
    #path('nosotros/', views.NosotrosView.as_view(), name='nosotros'),
    path('nosotros/', login_required(views.NosotrosView.as_view()), name='nosotros'),
    #path('delete/',  views.InicioView.delete, name='delete'),
    path('delete/<int:pk>/', views.deleteBook, name='delete'),
    path('new/', views.FormLibroNew.as_view(), name='new'), 
    path('edit/<int:pk>/', views.FormLibroEdit.as_view(), name='edit'),
    path('logout/', views.logout, name='logout')
]

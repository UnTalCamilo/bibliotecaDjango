from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #path('', views.InicioView.as_view(), name='inicio'),
    path('', login_required(views.InicioView.as_view()), name='inicio'),
    path('home/', login_required(views.InicioView.as_view()), name='home'),
    path('nosotros/', login_required(views.NosotrosView.as_view()), name='nosotros'),
    #path('delete/',  views.InicioView.delete, name='delete'),
    path('delete/<int:pk>/', login_required(views.deleteBook), name='delete'),
    path('new/', login_required(views.FormLibroNew.as_view()), name='new'),
    path('edit/<int:pk>/', login_required(views.FormLibroEdit.as_view()), name='edit'),
    path('accounts/logout/', views.CustomLogOutView.as_view(), name='logout'),
]


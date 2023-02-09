from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.InicioView.as_view(), name='inicio'),
    re_path(r'^nosotros/$', views.NosotrosView.as_view(), name='nosotros'),
    re_path(r'^libros/$', views.LibrosView.as_view(), name='libros'),
    re_path(r'^crear/$', views.CrearView.as_view(), name='crear'),
    re_path(r'^delete/$',  views.InicioView.deleteBook, name='delete'),
    # path('', views.inicio, name='inicio'),
    # path('nosotros/', views.nosotros, name='nosotros'),
    # path('crear/', views.crear, name='crear'),
]

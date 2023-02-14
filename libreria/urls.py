from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.InicioView.as_view(), name='inicio'),
    re_path(r'^nosotros/$', views.NosotrosView.as_view(), name='nosotros'),
    #re_path(r'^delete/$',  views.InicioView.delete, name='delete'),
    # re_path(r'^delete/(?P<pk>\d+)/$', views.eliminarView.as_view(), name='delete'),
    re_path(r'^new/$', views.subCategoriaNew.as_view(), name='new'),
    re_path(r'^edit/(?P<pk>\d+)/$', views.subCategoriaEdit.as_view(), name='edit')
]

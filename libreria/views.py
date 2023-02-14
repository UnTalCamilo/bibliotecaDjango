from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .forms import *
import os
from biblioteca.settings import MEDIA_ROOT
from django.core.paginator import Paginator
# Create your views here.


# def inicio(request):
#     #return HttpResponse("<h1>Bienvenido a la libreria</h1>")
#     return render(request, 'libreria/index.html')

# def nosotros(request):
#     return render(request, 'libreria/nosotros.html')

# def libros(request):
#     return render(request, 'libreria/libros.html')

# def crear(request):
#     return render(request, 'libreria/crear.html')

class InicioView(ListView):
    template_name = 'libreria/index.html'

    paginate_by = 2

    model = Libro
            


class NosotrosView(TemplateView):
    template_name = 'libreria/nosotros.html'

class LibrosView(TemplateView):
    template_name = 'libreria/libros.html'



class eliminarView(DeleteView):
    template_name = 'libreria/index.html'

    model = Libro

    context_object_name = 'libro'

    success_url = reverse_lazy('inicio')




class subCategoriaNew(CreateView):
    template_name = 'libreria/form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')

    

class subCategoriaEdit(UpdateView):
    template_name = 'libreria/form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')




from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from .forms import *
import os


class InicioView(ListView):
    template_name = 'libreria/index.html'

    paginate_by = 2

    model = Libro
            


class NosotrosView(TemplateView):
    template_name = 'libreria/about.html'


def deleteBook(request, pk):
    libro = Libro.objects.get(id=pk)
    try:
        img_path = libro.imagen.path
        os.remove(img_path)
    except Exception as e:
        print("No se pudo eliminar la imagen", e)
    libro.delete()
    return redirect('inicio')


 


class FormLibroNew(CreateView):
    template_name = 'libreria/form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')

    

    

    

class FormLibroEdit(UpdateView):
    template_name = 'libreria/form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')

def loginOut(request):
    logout(request)
    return redirect('inicio')
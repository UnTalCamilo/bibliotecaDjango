from pyexpat.errors import messages
from telnetlib import LOGOUT
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from biblioteca.settings import MEDIA_ROOT
from .forms import *
import os

class InicioView(ListView):
    template_name = 'libreria/index.html'

    paginate_by = 2

    model = Libro
            


class NosotrosView(TemplateView):
    template_name = 'libreria/about.html'


def deleteBook(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    try:
        os.remove(os.path.join(MEDIA_ROOT, libro.imagen.name))
    except:
        pass
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

class CustomLogOutView(LogoutView):
    
    template_name = 'registration/logout.html'

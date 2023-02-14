from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .forms import *
import os
from biblioteca.settings import MEDIA_ROOT
from django.core.paginator import Paginator


class InicioView(ListView):
    template_name = 'libreria/index.html'

    paginate_by = 2

    model = Libro
            


class NosotrosView(TemplateView):
    template_name = 'libreria/about.html'


class FormLibroDel(DeleteView):
    template_name = 'libreria/index.html'

    model = Libro

    context_object_name = 'libro'

    success_url = reverse_lazy('inicio')

    def get_initial(self):
        initial = super().get_initial()
        imagen = self.object.imagen
        try:
            os.remove(os.path.join(MEDIA_ROOT, imagen.name))
        except:
            pass
        return initial




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




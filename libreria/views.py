from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .forms import *
import os
from biblioteca.settings import MEDIA_ROOT
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

class InicioView(TemplateView):
    template_name = 'libreria/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.values()
        return context

    def delete(request):
        id = request.POST.get('id')
        try :
            book = Libro.objects.filter(id=id)
            os.remove(MEDIA_ROOT + '/' + str(book[0].imagen))
            book.delete()
            return render(request, 'libreria/index.html', {'libros': Libro.objects.values()})
        except:
            return render(request, 'libreria/index.html', {'libros': Libro.objects.values()})
            


class NosotrosView(TemplateView):
    template_name = 'libreria/nosotros.html'

class LibrosView(TemplateView):
    template_name = 'libreria/libros.html'

class CrearView(TemplateView):
    template_name = 'libreria/crear.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Titulo del libro'
        context['imagen'] = 'imagen del libro'
        context['descripcion'] = 'descripcion del libro'
        print("context: ", context)
        return context
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = LibroForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            context['form'] = LibroForm() 
        else:
            context['form'] = form
        return self.render_to_response(context)


class eliminarView(DeleteView):
    template_name = 'libreria/index.html'

    model = Libro

    context_object_name = 'libro'

    success_url = reverse_lazy('inicio')




class subCategoriaNew(CreateView):
    template_name = 'libreria/subcategoria_form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')

    

class subCategoriaEdit(UpdateView):
    template_name = 'libreria/subcategoria_form.html'

    model = Libro

    context_object_name = 'libro'

    form_class = LibroForm

    success_url = reverse_lazy('inicio')




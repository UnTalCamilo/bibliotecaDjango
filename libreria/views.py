from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
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
        print("context: ", context)
        return context

    def deleteBook():
        pass


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
            print("form: ", form)
            form.save()
            context['form'] = LibroForm() 
        else:
            context['form'] = form
        return self.render_to_response(context)
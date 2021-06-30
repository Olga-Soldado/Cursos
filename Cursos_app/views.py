from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Cursos
# Create your views here.
def home(request):
    return redirect('/main')

def index(request):
    context = {
        "inf": Cursos.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    errors = Cursos.objects.cursos_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/main')
    else:
        Cursos.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        )
        messages.success(request, 'Se creo un nuevo curso')
        return redirect("/main")

def confirmar(request,id):
    context = {
        "Cursos": Cursos.objects.get(id=id)
    }
    return render(request, "eliminar.html",context)

def destroy(request, id):
    Cursos.objects.get(id=id).delete()
    messages.success(request,'Se elimino correctamente. ')
    return redirect('/main')


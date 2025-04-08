from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def registro_log(request):
    return render(request, 'log_regis.html')

def index(request):
    return render(request, 'index.html')

def adminis(request):
    return render (request, 'index_admin.html')

def acercade(request):
    return render(request, 'SobreNosotros.html')

def contacto(request):
    return render(request, 'Contactenos.html')


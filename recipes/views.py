from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')  # Pagina Home

# def home(request):
#     return HttpResponse('Home')  # Pagina Home

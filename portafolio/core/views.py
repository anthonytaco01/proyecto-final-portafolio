from django.shortcuts import render

# Creacion de pestañas
def home (request):
    return render(request, 'core/home.html') 

def contact(request):
    return render(request, 'core/contact.html')

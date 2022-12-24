from django.shortcuts import render


def portal(request, usuario):
    return render(request, "Portal.html", {"mensaje": f"bienvenido {usuario}"})


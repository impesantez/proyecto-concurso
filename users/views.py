from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Las contraseñas no son iguales.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El email ya está en uso.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'signup.html')

        try:
            user = User(
                name=name,
                username=username,
                email=email,
                password=make_password(password),
            )
            user.save()
            messages.success(request, "Cuenta creada con éxito. ¡Por favor, inicia sesión!")
            return redirect('users:login')
        except Exception as e:
            messages.error(request, f"Error al crear la cuenta: {e}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

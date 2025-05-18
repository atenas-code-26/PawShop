from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import MinimalUserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = MinimalUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MinimalUserChangeForm(instance=request.user)
    return render(request, 'accounts/editar_usuario.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


    
from django.shortcuts import render, redirect

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    # регистрирует нового пользователя
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # выполнение входа и перенаправление на дом. страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

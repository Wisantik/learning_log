from django.shortcuts import render, redirect

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

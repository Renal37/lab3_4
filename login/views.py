from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect('/login')

        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login/login.html')

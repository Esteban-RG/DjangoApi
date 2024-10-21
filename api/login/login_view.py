from django.shortcuts import render

def login_view(request):
    template_view = "auth-login.html"

    return render(request,template_view)
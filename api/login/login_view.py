from django.shortcuts import render

def login_view(request):
    template_view = "sign-in.html"

    return render(request,template_view)

def register_view(request):
    template_view = "sign-up.html"

    return render(request,template_view)

def forgot_view(request):
    template_view = "auth-forgot-password.html"

    return render(request,template_view)
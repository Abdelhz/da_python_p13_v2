from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})


def custom_server_error_view(request):
    return render(request, "errors/500.html", {})

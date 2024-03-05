from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def index(request):
    return render(request, 'index.html')


def custom_page_not_found_view(request, exception):
    response = render(request, "errors/404.html", {})
    return HttpResponseNotFound(response.content)


def custom_server_error_view(request):
    response = render(request, "errors/500.html", {})
    return HttpResponseServerError(response.content)

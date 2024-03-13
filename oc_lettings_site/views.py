from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Handles the 'index' request and renders the 'index.html' template.

    This function attempts to render the 'index.html' template.
    If an exception occurs during rendering, it is logged and re-raised.

    :param request: HttpRequest object that contains metadata about the request.
    :return: HttpResponse object with the rendered text (HTML code) of the 'index.html' template.
    :raises: Exception if there is an error during rendering.

    """
    try:
        return render(request, 'index.html')
    except Exception as e:
        logger.error(e)
        raise


def custom_page_not_found_view(request, exception):
    """
    Custom view to handle 404 (page not found) errors. Renders a custom 404 error page.

    This function attempts to render a custom 404 error page.
    If an exception occurs during rendering, it is logged and re-raised.

    :param request: HttpRequest object that contains metadata about the request.
    :param exception: Exception object that contains information about the exception triggered.
    :return: HttpResponseNotFound object with the rendered text (HTML code)
    of the '404.html' template.
    :raises: Exception if there is an error during rendering.

    """
    try:
        response = render(request, "errors/404.html", {})
        return HttpResponseNotFound(response.content)
    except Exception as e:
        logger.error(e)
        raise


def custom_server_error_view(request):
    """
    Custom view to handle 500 (internal server error) errors. Renders a custom 500 error page.

    This function attempts to render a custom 500 error page.
    If an exception occurs during rendering, it is logged and re-raised.

    :param request: HttpRequest object that contains metadata about the request.
    :return: HttpResponseServerError object with the rendered text (HTML code)
    of the '500.html' template.
    :raises: Exception if there is an error during rendering.
    """
    try:
        response = render(request, "errors/500.html", {})
        return HttpResponseServerError(response.content)
    except Exception as e:
        logger.error(e)
        raise

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Django view function to display a list of all lettings.

    This function retrieves all Letting objects from the database and passes them
    to the 'lettings/index.html' template in the 'lettings_list' context variable.
    If an error occurs during this process, it logs the error and raises an
    Http404 exception with a custom error message.

    :param request: The HTTP request object.
    :return: A render() call that combines the 'lettings/index.html' template
    with the context variable.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving lettings")


def letting(request, letting_id):
    """
    Django view function to display a specific letting.

    This function retrieves a Letting object with the given ID from the database and
    passes its title and address to the 'lettings/letting.html' template in the 'title' and
    'address' context variables. If the Letting object does not exist or an
    error occurs during this process,
    it logs the error and raises an Http404 exception with a custom error message.

    :param request: The HTTP request object.
    :param letting_id: The ID of the letting to display.
    :return: A render() call that combines the 'lettings/letting.html' template with
    the context variable.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving letting")

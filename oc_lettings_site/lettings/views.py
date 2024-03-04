from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting
import logging


logger = logging.getLogger(__name__)


def index(request):
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving lettings")


def letting(request, letting_id):
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

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Handles the 'index' request and renders a list of all profiles.

    :param request: HttpRequest object that contains metadata about the request.
    :return: HttpResponse object with the rendered text (HTML code) of the 'profiles/index.html'
    template.
    :raises Http404: If there is an error retrieving profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving profiles")


def profile(request, username):
    """
    Handles a request for a specific profile and renders that profile's detail view.

    :param request: HttpRequest object that contains metadata about the request.
    :param username: The username of the profile to retrieve.
    :return: HttpResponse object with the rendered text (HTML code) of the 'profiles/profile.html'
    template.
    :raises Http404: If there is an error retrieving the profile.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving profile")

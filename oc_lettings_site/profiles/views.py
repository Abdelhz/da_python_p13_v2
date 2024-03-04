from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile
import logging


logger = logging.getLogger(__name__)


def index(request):
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving profiles")


def profile(request, username):
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(e)
        raise Http404("Error retrieving profile")

from django.contrib import auth
from django.shortcuts import render, render_to_response

# Create your views here.
from basic_parser.models import Profile


def basic(request, profile_id):
    args = {}
    profile = Profile.objects.get(pk=profile_id)
    args['name'] = profile.name
    args['user'] = auth.get_user(request)
    return render_to_response('profile_page.html', args)
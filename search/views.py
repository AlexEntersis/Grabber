from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from pandas.io import json
from basic_parser.models import Profile, Skills
from search.forms import SearchForm
from collections import OrderedDict

def profiles_dict(profiles):
    profiles_info = [{"pk": profile.pk,
                      "name": profile.name[:20] + "..." if len(profile.name) > 25 else profile.name,
                      "title": profile.title[:25] + "..." if len(profile.title) > 25 else profile.title,
                      "url":  profile.url,
                      "email": profile.email,
                      "phone": profile.phone,
                      "skills": list(OrderedDict.fromkeys([skill.skill_name for skill in Skills.objects.filter(profile=profile)]).keys()),
                      } for profile in profiles]
    return profiles_info

def ajax_search(request):
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                data = {}
                data['search_args'] = [str(request.POST.get('title')),
                                       str(request.POST.get('skill')).lower(),
                                       str(request.POST.get('location')).lower().capitalize(),]
                profiles = profile_filter(data['search_args'])
                data['profiles'] = profiles_dict(profiles)
                data['page_limit'] = 30 if len(data['profiles']) >= 30 else len(data['profiles'])
                return HttpResponse(json.dumps(data), content_type="application/json")


def profile_filter(param):
    profiles = Profile.objects.all()
    if param[0]:
        profiles = profiles.filter(title__icontains=param[0])
    if param[1]:
        profiles = profiles.filter(skills__skill_name=param[1]).distinct()
    if param[2]:
        profiles = profiles.filter(address=param[2])
    return profiles

def basic(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            args = dict()
            args['form'] = SearchForm
            args['user'] = auth.get_user(request)
            return render_to_response('result.html', args)
    else:
        form = SearchForm()
    return render(request, 'result.html', {'form': form})


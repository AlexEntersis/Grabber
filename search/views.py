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

def profile_paginator(profiles, page_limit, page_number):
    start_of_page = page_number * page_limit
    end_of_page = (page_number * page_limit) + page_limit
    new_profiles = profiles[start_of_page:end_of_page]
    return new_profiles

def ajax_search(request):
        profiles_per_page = 25  # indicated how many profiles will be shown on one page
        page = int(request.POST.get('page')) - 1
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                data = {}
                data['search_args'] = [str(request.POST.get('title')),
                                       str(request.POST.get('skill')).lower(),
                                       str(request.POST.get('location')).lower().capitalize()]
                if not str(request.POST.get('title')) and not str(request.POST.get('skill')) and not str(request.POST.get('location')):
                    data['empty_search_args'] = True
                else:
                    data['empty_search_args'] = False
                    profiles = profile_filter(data['search_args'])
                    data['total_number_profiles'] = len(profiles)
                    profiles = profile_paginator(profiles, profiles_per_page, page)
                    data['profiles'] = profiles_dict(profiles)
                    data['page'] = page + 1
                    data['number_of_pages'] =  data['total_number_profiles'] // profiles_per_page
                    data['page_limit'] = profiles_per_page if len(data['profiles']) >= profiles_per_page else len(data['profiles'])
                return HttpResponse(json.dumps(data), content_type="application/json")

def profile_filter(param):
    profiles = Profile.objects.all()
    if param[0]:
        profiles = profiles.filter(title__icontains=param[0]).distinct()
    if param[1]:
        profiles = profiles.filter(skills__skill_name=param[1]).distinct()
    if param[2]:
        profiles = profiles.filter(address=param[2]).distinct()
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


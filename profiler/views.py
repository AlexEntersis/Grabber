import datetime
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from basic_parser.models import Profile
from pandas.io import json
from profiler.models import Comments

def basic(request, profile_id):
    if request.method == 'GET':
            args = dict()
            args['user'] = auth.get_user(request)
            args['profile'] = Profile.objects.get(pk=profile_id)
            return render_to_response('profile_page.html', args)
    return render(request, 'profile_page.html')


def all_comments(request, profile_id):
    data = {}
    data['comments'] = [{'comment_text': comment.comment_text,
                         'comment_author': comment.comment_author,
                         'comment_date': comment.comment_date.isoformat(),
                         'comment_vacancy': comment.comment_vacancy}
                        for comment in Comments.objects.filter(profile=Profile.objects.get(pk=profile_id))]
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_comment(request, profile_id):
    data = {}
    data['profile_name'] = Profile.objects.get(pk=profile_id).name
    data['comment_author'] = auth.get_user(request).username
    data['comment_vacancy'] = request.POST.get('selected_opening')
    if request.POST.get('comment_text'):
        data['comment_text'] = request.POST.get('comment_text')
    new_comment = Comments(comment_author=data['comment_author'],
                           comment_text=data['comment_text'],
                           comment_vacancy=data['comment_vacancy'],
                           comment_date=datetime.datetime.now().today())
    new_comment.save()
    profile = Profile.objects.get(pk=profile_id)
    profile.comments.add(new_comment)
    return HttpResponse(json.dumps(data), content_type="application/json")

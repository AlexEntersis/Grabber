import datetime
from django.contrib import auth
from django.shortcuts import render, render_to_response
from basic_parser.models import Profile
from profiler.forms import CommentForm
from profiler.models import Comments


def basic(request, profile_id):
    if request.method == 'GET':
        form = CommentForm(request.GET)
        if form.is_valid():
            args = {}
            profile = Profile.objects.get(pk=profile_id)
            args['name'] = profile.name
            args['user'] = auth.get_user(request)
            args['form'] = form
            return render_to_response('profile_page.html', args)
    else:
        form = CommentForm(request.GET)
    return render(request, 'profile_page.html', {'form': form})

def add_comment(request):
    args = {}
    new_comment = Comments(comment_author="ME",
                           comment_text="BLAH",
                           comment_date=datetime.datetime.now().today())
    new_comment.save()
    profile = Profile.objects.get(pk=1747)
    profile.comments.add(new_comment)
    return render_to_response('profile_page.html', args)
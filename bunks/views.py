from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Bunk
# Create your views here.

class FeedView(generic.ListView):
    template_name = 'bunks/feed.html'
    context_object_name = 'bunk_list'
    model = Bunk

    # def get_context_data(self, **kwargs):
    #     """Add to context, Return dictionary."""
    #     context = super(FeedView, self).get_context_data(**kwargs)
    #     context['']

class UserFeedView(generic.ListView):
    template_name = 'bunks/user_feed.html'
    context_object_name = 'bunk_list'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Bunk.objects.filter(
            to_user=get_object_or_404(User, username=self.kwargs['username']).id
        )

    def get_context_data(self, **kwargs):
        context = super(UserFeedView, self).get_context_data(**kwargs)
        context['kwargs']=self.kwargs
        return context

def bunk(request, username):
    to_username = request.POST['to_user']
    try:
        from_user=User.objects.get(username=username)
        to_user=User.objects.get(username=to_username)
        bunk = Bunk(from_user=from_user, to_user=to_user)
    except (KeyError, User.DoesNotExist):
        return render(request, 'bunks/user_feed.html', {
            'bunk_list': from_user.bunks_in.all(),
            'error_message': to_username+ " not found.",
            'user': request.POST['to_user'],
            'kwargs': {'username': username}
        })
    else:
        bunk.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bunks:user_feed', args=(to_user.username,)))
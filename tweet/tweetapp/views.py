from django.shortcuts import render
from .models import Tweet, User
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

#to list all the tweets on a page :
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    data = {
        'tweets' : tweets
    }

    return render(request, 'list_all.html', data)

#to create the tweets :
@login_required
def create_tweet(request):
    if request.method == 'POST' :
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) #don't yet add this object to data base 
            tweet.user = request.user
            tweet.save() #now save this object to data base as it contains the info of user as well 
            return redirect('list-all')
    else:
        form = TweetForm()

    data = {
        'form' : form
    }

    return render(request, 'tweet_form.html', data)

#update the tweet form : 
@login_required
def update_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('list-all')
    else:
        form = TweetForm(instance=tweet)

    data = {
        'form' : form
    }

    return render(request, 'tweet_form.html', data)

#delete the tweet : 
@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('list-all')

    data = {
        'tweet' : tweet
    }

    return render(request, 'tweet_confirm_delete.html', data)

#create a view which allows the user to register : 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('list-all')
    else:
        form = UserRegistrationForm()

    data = {
        'form': form
    }

    return render(request, 'registration/register.html', data)

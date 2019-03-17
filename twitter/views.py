from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic, View

from twitter import forms
from twitter.forms import UserRegisterForm
from twitter.models import Tweet


class MainPageView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')


class RegisterView(View):
    template_name = 'twitter/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('/')

        return render(request, self.template_name, {'form': form})


class AddTweetView(generic.CreateView):
    model = Tweet
    form_class = forms.TweetFrom
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfileView(View, LoginRequiredMixin):
    template_name = 'twitter/user_profile.html'

    def get(self, request):
        user = request.user
        tweets = Tweet.objects.filter(author=user).order_by('-creation_date')
        return render(request, self.template_name, {'tweets': tweets})


class TweetDetailsView(View):
    template_name = 'twitter/tweet_details.html'

    def get(self, request, tweet_id):
        tweet = Tweet.objects.get(id=tweet_id)
        return render(request, self.template_name, {'tweet': tweet})


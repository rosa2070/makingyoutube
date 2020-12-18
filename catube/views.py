from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F
from django.shortcuts import render, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Video, Comment
from .forms import VideoForm, CommentForm


class VideoListView(ListView):
    model = Video
#    paginate_by = 4



class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'

    def form_valid(self, form):
        video = form.save(commit=False)
        video.author= self.request.user
        return super().form_valid(form)


class VideoDetailView(DetailView):
    model = Video


class VideoUpdateView(UserPassesTestMixin, UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'

    def test_func(self):
        return self.request.user == self.get_object().author


class VideoDeleteView(UserPassesTestMixin, DeleteView):
    model = Video

    def test_func(self):
        return self.request.user == self.get_object().author
# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

# Add this view
class GamePageView(TemplateView):
    template_name = "game.html"

# Add this view
class LearnPageView(TemplateView):
    template_name = "learn.html"

class DiyPageView(TemplateView):
    template_name = "diy.html"

class HomePageView(TemplateView):
    template_name = "home.html"

# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^game/$', views.GamePageView.as_view()),
    url(r'^learn/$', views.LearnPageView.as_view()),
    url(r'^diy/$', views.DiyPageView.as_view()),
    url(r'^home/$', views.HomePageView.as_view()),




]

from django.conf.urls import patterns, url
from RESTSChrome import views


urlpatterns = patterns('RESTSChrome.views',
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),
    url(r'^image_book/$', views.ImageBookListView.as_view()),
    url(r'^image_book/(?P<pk>[0-9]+)/$', views.ImageBookDetailView.as_view()),
    url(r'^images/$', views.ImageListView.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetailView.as_view()),
    url(r'^image_text/$', views.ImageTextListView.as_view()),
    url(r'^image_text/(?P<pk>[0-9]+)/$', views.ImageTextDetailView.as_view()),
)
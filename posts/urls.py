from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'), # if root, we want to get posts view with that name
    url(r'^(?P<pk>\d+)$', post_detail, name='post_detail'), # if it's passed in with an ID (pk group), we want to open the post_detail view
    url(r'^new/$', create_or_edit_post, name="new_post"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name="edit_post")
]
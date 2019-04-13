"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # method include includes extra URL files
from django.contrib import admin
from django.views.generic import RedirectView # redirect to a view
from django.views.static import serve
from .settings import MEDIA_ROOT # need to import it to serve out our MEDIA_URL

# ^ is for beginning of line, $ is for end of line

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='posts/')), # if someone goes to the root dir, we want to redirect them posts
    url(r'posts/', include('posts.urls')), # if somebody goes to the posts URL, then we want it to be passed using the URLs in the urls.py file in the posts app.
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}) # point towards a <path> to a particular file and we're going to serve up the document_root
]


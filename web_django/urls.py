from django.conf.urls import include, url
from django.contrib import admin
from blog import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'web_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^blog/',views.blog_index),
]

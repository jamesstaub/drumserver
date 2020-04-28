from django.urls import path, re_path, include

from django.contrib import admin

admin.autodiscover()

import api.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [

    re_path(r'^search/*', api.views.search, name="search"),
    re_path(r'^', api.views.index, name="drumserver"),
    
    # path("admin/", admin.site.urls),
]



# urlpatterns = [
#     re_path(r'^index/$', api.views.index, name='index'),
#     re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
#     re_path(r'^weblog/', include('blog.urls')),
# ]
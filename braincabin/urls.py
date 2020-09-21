# BrainCabin URL Configuration


from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('graphql/', include('graphqlAPI.urls')),
    path('', lambda request: redirect('/account/register')),
]

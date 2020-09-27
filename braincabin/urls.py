# BrainCabin URL Configuration


from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def rootRedirect(request):
    if request.user.is_anonymous:
        return redirect('login')
    return redirect('forum-questions')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls.account_urls')),
    path('users/', include('users.urls.users_urls')),
    path('forum/', include('forum.urls')),
    path('graphql/', include('graphqlAPI.urls')),
    path('', rootRedirect),
]

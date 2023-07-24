"""popmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from movies .views import movie_create,home_movie,view_movie,delete_movie,update_movie,About,send_gmail,all_movies,user_signup,user_login,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',movie_create, name='create_movies'),
    path('', home_movie, name='list_movies'),
    path('all/', all_movies, name='all_movies'),
    path('about/',About, name='about'),
    path('contact/',send_gmail,name='contact'),
    path('<int:pk>/', view_movie, name='view_movies'),
    path('<int:pk>/update/', update_movie, name='update_movies'),
    path('<int:pk>/delete/', delete_movie, name='delete_movies'),
    path('signup/', user_signup,name='signup'),
    path('login/', user_login,name='login'),
    path('logout/',user_logout,name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


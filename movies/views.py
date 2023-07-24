from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core import mail
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from  .forms import signupform,loginform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout






def movie_create(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        form = MovieForm()
    return render(request, 'create-movie.html', {'form': form})
  else:
      return HttpResponseRedirect('/login/')

def home_movie(request):
 if request.user.is_authenticated:
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})
 else:
      return HttpResponseRedirect('/login/')

def view_movie(request, pk):
 if request.user.is_authenticated:
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'view-movie.html', {'movie': movie})
 else:
      return HttpResponseRedirect('/login/')

def update_movie(request, pk):
 if request.user.is_authenticated:
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('view_movies', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'update-movie.html', {'form': form})
 else:
      return HttpResponseRedirect('/login/')

def delete_movie(request, pk):
 if request.user.is_authenticated:
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('list_movies')
    return render(request, 'delete-movie.html', {'movie': movie})
 else:
      return HttpResponseRedirect('/login/')


def About(request):
    return render(request, 'about.html')



def all_movies(request):
 if request.user.is_authenticated:
    movies = Movie.objects.all()
    return render(request, 'allmovies.html', {'movies': movies})
 else:
      return HttpResponseRedirect('/login/')



def send_gmail(request):
     if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         message = request.POST.get('message')
         print(name,email,phone,message)

         '''subject = ('name of the person :',name + 'Email of the person: ',email +'contact number of the person:', phone )'''

         subject = 'Contact form'

         message = f'name of the person: {name}, \n  Email of the person: {email}, \n contact number of the person: {phone}, \n message from the person: {message} ' 

         

         send_mail(
             subject,
            
             
             message,
             'kunzoro34@gmail.com',
             ['popsonemmanuel99@gmail.com'],
             fail_silently=False,
             
         )
          
         return HttpResponseRedirect(reverse('list_movies'))
         
     else:
         
          
         return render(request,'contact.html')



#logout
def user_logout(request):
 if request.user.is_authenticated:
    logout(request)
    return redirect('list_movies')
 else:
      return HttpResponseRedirect('/login/')

#signup
def user_signup(request):
 if request.method == "POST":
    form = signupform(request.POST)
    if form.is_valid():
        messages.success(request, "Congratulations!! Welcome to Movie Box. ")
        user= form.save()
        
 else:
  form = signupform()
 return render(request, 'signup.html', {'form':form})

#login
def user_login(request):
 if not request.user.is_authenticated:
      if request.method == "POST":
            form = loginform( data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully !!')
                    #return HttpResponseRedirect('/list_cakes/')
                    return redirect('list_movies')
      else:
            form = loginform()
      return render(request, 'login.html', {'form': form})
 else:
    return HttpResponseRedirect('')
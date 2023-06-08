from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,ListView,UpdateView,CreateView,DeleteView,DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from.forms import *
from.models import *
from django.db.models import Q
WSGIRequest
from.utils import *
from django.core.paginator import Paginator




class Main(DataMixin,ListView):
    model = Movie
    template_name ='index.html'
    context_object_name ='films'
    paginate_by =3
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        cdef=self.get_user_context(title='Головна')
        year = self.request.GET.getlist('year', '')
        genre_list=self.request.GET.getlist('genre_name','')
        year_genre = Movie.objects.filter(Q(genres__in=genre_list) | Q(year__in=year)).distinct()
        search_quary= self.request.GET.get('search','')
        search_movies = Movie.objects.filter(Q(title__icontains=search_quary) | Q(english_title__icontains=search_quary))
        if year or genre_list:
            context['movies']=year_genre
        elif search_quary:
            context['movies']=search_movies
        else:
            context['movies']=context['films']

        return dict(list(context.items())+list(cdef.items()))




class FilmDetail(View):
    def get(self,request,id):
        film=Movie.objects.prefetch_related('actors').get(id=id)
        genres=Genre.objects.all()
        form=ReviewsForm()
        star_form=RatingForm()
        return render(request, 'movies/film_detail.html',context={'film': film,'star_form':star_form, 'genres': genres, 'form': form})

    def post(self,request,id):
        form=ReviewsForm(request.POST)
        film = Movie.objects.get(id=id)
        genres = Genre.objects.all()
        if form.is_valid():
            form=form.save(commit=False)
            form.movie_id=id
            form.save()
            return redirect(film)

        return render(request,'movies/film_detail.html',context={'film':film,'form':form,'genres':genres})


class AddRating(View):
    def get_client_ip(self,request):
        x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip=x_forwarded_for.split(',')[0]
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip

    def post(self,request):
        rating_form=RatingForm(request.POST)
        if rating_form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=request.POST.get('movie'),
                defaults={'star_id':int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)





class GenreDetail(DataMixin,ListView):
    model = Genre
    template_name = 'movies/genre_detail.html'
    context_object_name = 'movies'
    paginate_by =3
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['genre_object']=Genre.objects.get(url__iexact=self.kwargs['url'])
        context['films']=Movie.objects.all()
        cdef=self.get_user_context(title=context['genre_object'].name)
        return dict(list(context.items())+list(cdef.items()))

    def get_queryset(self):
        return Genre.objects.get(url__iexact=self.kwargs['url']).film_genres.all()



class ActorDetail(DataMixin,DetailView):
    model = Actor
    pk_url_kwarg ='id'
    context_object_name='actor'
    template_name = 'movies/actor_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cdef=self.get_user_context(title=context['actor'].name)
        return dict(list(context.items())+list(cdef.items()))

class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name ='movies/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['films']=Movie.objects.all()
        cdef=self.get_user_context(title='Реєстрація')
        return dict(list(context.items()) + list(cdef.items()))




class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'movies/login.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cdef=self.get_user_context(title='Авторизація')
        return dict(list(context.items()) + list(cdef.items()))

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    """Вихід з профіля"""
    logout(request)
    return redirect('login')
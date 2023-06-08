from django.db import models
from datetime import date
from django.shortcuts import reverse




class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Категорія')
    description=models.TextField(verbose_name='Опис')
    url=models.SlugField(max_length=160,unique=True,verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категорія'
        verbose_name_plural='Категорії'


class Actor(models.Model):
    name=models.CharField(max_length=100,verbose_name='Імя')
    english_name=models.CharField(max_length=100,verbose_name='Імя на англійській',null=True)
    age=models.DateField(default=date.today,verbose_name='Вік')
    description=models.TextField(verbose_name='Опис')
    image=models.ImageField(upload_to='actors/',verbose_name='Зображення')
    height=models.DecimalField(max_digits=3,decimal_places=2,verbose_name='Зріст',null=True)
    devorced=models.ManyToManyField('self',related_name='devorced_related',verbose_name='Розлучення',blank=True)
    married=models.OneToOneField('self',on_delete=models.SET_NULL,related_name='wife_or_husband',verbose_name='Шлюб',null=True,blank=True)
    native_country=models.CharField(max_length=100 ,verbose_name='Місто народження',null=True)
    genres=models.ManyToManyField('Genre',verbose_name='Жанри',related_name='film_genre',blank=True)
    gender=models.ForeignKey('Gender',on_delete=models.CASCADE,verbose_name='Стать')
    sum_movies = models.PositiveSmallIntegerField(verbose_name='Кількість фільмів',default=0,null=True)


    def get_absolute_url(self):
        return reverse('actor_detail_url',kwargs={'id':self.id})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Людина'
        verbose_name_plural='Люди'



class Genre(models.Model):
    name=models.CharField(max_length=100,verbose_name='Ім`я')
    description=models.TextField(verbose_name='Опис')
    url=models.SlugField(max_length=100,unique=True,verbose_name='Слаг')

    def get_absolute_url(self):
        return reverse('genre_detail_url',kwargs={'url':self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанри'


class Movie(models.Model):
    title=models.CharField(max_length=100,verbose_name='Назва')
    english_title=models.CharField(max_length=100,verbose_name='Назва на англійській',null=True)
    tagline=models.CharField(max_length=100,default=' ',verbose_name='Слоган')
    description=models.TextField(verbose_name='Опис')
    description_2 = models.TextField(verbose_name='Докладний опис',null=True)
    poster=models.ImageField(upload_to='movies/',verbose_name='Постер')
    year=models.PositiveSmallIntegerField(default=2019,verbose_name='Дата виходу')
    country=models.CharField(max_length=30,verbose_name='Країна')
    directors=models.ManyToManyField(Actor,verbose_name='Режисер',related_name='film_director')
    actors=models.ManyToManyField(Actor,verbose_name='Актори',related_name='film_actor')
    genres=models.ManyToManyField(Genre,verbose_name='Жанри',related_name='film_genres')
    world_premiere=models.DateField(default=date.today,verbose_name='Прем`єра у світі')
    ukrainian_premiere = models.DateField(default=date.today, verbose_name='Прем`єра в Україні')
    budget=models.PositiveIntegerField(default=0,help_text='вказувати суму у доларах',verbose_name='Бюджет')
    fees_in_usa= models.PositiveIntegerField( default=0, help_text='вказувати суму у доларах',verbose_name='Збори в США')
    fees_in_world = models.PositiveIntegerField( default=0, help_text='вказувати суму у доларах',verbose_name='Збори у світі')
    category=models.ForeignKey(Category,verbose_name='Категорія',on_delete=models.SET_NULL,null=True)
    url=models.SlugField(max_length=130,unique=True,verbose_name='Слаг')
    draft=models.BooleanField(default=False,verbose_name='Чернетка')
    age=models.PositiveSmallIntegerField(default=0,verbose_name='Вік')
    scenarists = models.ManyToManyField(Actor, verbose_name='Сценарій', related_name='film_scenarist')
    compositors=models.ManyToManyField(Actor,verbose_name='Композитор',related_name='film_compositor')
    hudogniks=models.ManyToManyField(Actor,verbose_name='Художник',related_name='film_hudognik')
    operators=models.ManyToManyField(Actor,verbose_name='Оператор',related_name='film_operators')
    producer = models.ManyToManyField(Actor, verbose_name='Продюсер', related_name='film_producers')
    treiler=models.FileField(upload_to='treilers/',verbose_name='Трейлер',null=True)
    quality_videos=models.ForeignKey('QualityVideos',on_delete=models.SET_NULL,null=True,verbose_name='Якість відео')


    def get_absolute_url(self):
        return reverse('film_detail_url',kwargs={'id':self.id})


    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Фільм'
        verbose_name_plural='Фільми'


class MovieShots(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    description=models.TextField(verbose_name='Опис')
    image=models.ImageField(upload_to='movie_shots/',verbose_name='Фото')
    movie=models.ForeignKey(Movie,related_name='movieshots',verbose_name='Фільм',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Кадр з фільму'
        verbose_name_plural='Кадри з фільму'


class RatingStar(models.Model):
    value=models.PositiveSmallIntegerField(default=0,verbose_name='Значення')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name='Зірка рейтингу'
        verbose_name_plural='Зірки рейтингу'
        ordering=['-value']

class Rating(models.Model):
    ip=models.CharField(max_length=15,verbose_name='IP адреса')
    star=models.ForeignKey(RatingStar,on_delete=models.CASCADE,verbose_name='зірка')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='фільм')

    def str(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural='Рейтинги'


class Reviews(models.Model):
    email=models.EmailField(verbose_name='Email')
    name=models.CharField(max_length=100,verbose_name='І`мя')
    text=models.TextField(max_length=5000,verbose_name='Ваш коментарій')
    parent=models.ForeignKey('self',verbose_name='Батько',on_delete=models.SET_NULL,blank=True,null=True)
    movie=models.ForeignKey(Movie,verbose_name='Фільм',on_delete=models.CASCADE,related_name='review_movie')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name='Відгук'
        verbose_name_plural='Відгуки'


class Gender(models.Model):
    title=models.CharField(max_length=20,verbose_name='Вік')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вік'
        verbose_name_plural = 'Вік'


class QualityVideos(models.Model):
    title=models.CharField(max_length=20,verbose_name='Найменування якості')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Якість відео'
        verbose_name_plural = 'Якість відео'



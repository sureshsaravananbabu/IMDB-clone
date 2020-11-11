from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import movie,movielinks,cast
from django.views.generic.dates import YearArchiveView

# Create your views here.
class MovieList(ListView):
    model=movie
    paginate_by = 3


class MostWatch(ListView):
    model = movie
    paginate_by = 20
    template_name='movie/mostwatched.html'  
    def get_context_data(self,**kwargs):
        context=super(MostWatch,self).get_context_data(**kwargs)
        context['object_list']=movie.objects.all()
        return context


class HomeView(ListView):
    model = movie
    template_name='movie/home.html'
    def get_context_data(self,**kwargs):
        context=super(HomeView,self).get_context_data(**kwargs)
        context['top_rated']=movie.objects.filter(status='TR')
        context['most_watched']=movie.objects.filter(status='MW')
        context['recently_added']=movie.objects.filter(status='RA')
        print(context['recently_added'])
        return context

class MovieDetail(DetailView):
    model=movie

    def get_object(self):
        object=super().get_object()
        object.save()
        return object

    def get_context_data(self,**kwargs):
        print(self)
        context=super(MovieDetail,self).get_context_data(**kwargs)
        context['related_movies']=movie.objects.filter(category__contains=self.get_object().category).exclude(slug=self.get_object().slug)
        context['cast']=cast.objects.filter(movie=self.get_object())
        context['links']= movielinks.objects.filter(movie=self.get_object())
        context['views']=int(movie.objects.filter(title=self.get_object()).values('views_count')[0]['views_count'])
        movie.objects.filter(title=self.get_object()).update(views_count=context['views']+1)
        return context
class MovieCategory(ListView):
    model = movie
    paginate_by = 4

    def get_queryset(self):
        self.category=self.kwargs['category']
        movies=movie.objects.filter(category__contains=self.category)
        return movies
    def get_context_data(self,**kwargs):
        context=super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']= self.category
        return context

class MovieLanguage(ListView):
    model = movie
    paginate_by = 4

    def get_queryset(self):
        print(self)
        self.language=self.kwargs['lang']
        movies=movie.objects.filter(language=self.language)
        return movies
    def get_context_data(self,**kwargs):
        print(self)
        context=super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language']= self.language
        return context


class MovieSearch(ListView):
    model = movie
    paginate_by = 4

    def get_queryset(self):
        query=self.request.GET.get('s')
        print(query)
        if query:
            object_list=movie.objects.filter(title__icontains=query)
        else:
            object_list=self.model.objects.none()
        return object_list

class MovieYear(ListView):
    model=movie
    paginate_by = 4
    def get_queryset(self):
        self.year=self.kwargs['year']
        movies=movie.objects.filter(year_of_production__year=self.year)
        return movies
    def get_context_data(self,**kwargs):
        context=super(MovieYear,self).get_context_data(**kwargs)
        context['movie_Year']= self.year
        return context 

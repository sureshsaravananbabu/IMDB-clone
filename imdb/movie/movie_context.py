from .models import movie

def  slider_movies(request):
    movies=movie.objects.all().order_by('created')[0:4]
    return {'slider_movies':movies}
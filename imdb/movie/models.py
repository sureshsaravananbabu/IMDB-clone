from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField

CATEGORY_CHOICES =(
    ('action','ACTION'),
    ('biography','BIOGAPHY'),
    ('drama','DRAMA',),
    ('comedy','COMEDY'),
    ('romance','ROMANCE',),
)


LANGUAGE_CHOICES=(
    ('english','ENGLISH'),
    ('german','GERMAN'),
)
STATUS_CHOICES=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),

)
# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='movies')
    banner=models.ImageField(upload_to='movies_banner')
    category=MultiSelectField(choices=CATEGORY_CHOICES)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=10)
    status=models.CharField(choices=STATUS_CHOICES,max_length=2)
    year_of_production=models.DateField()
    views_count=models.IntegerField(default=0)
    slug=models.SlugField(blank=True,null=True)
    video = EmbedVideoField()
    created=models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title
LINK_CHOICES=(
('D','DOWNLOAD LINK'),
('W','WATCH LINK'),
)

class movielinks(models.Model):
    movie=models.ForeignKey(movie,related_name='movie_watch_link',on_delete=models.CASCADE)
    link=models.URLField()
    type=models.CharField(choices=LINK_CHOICES,max_length=1)

    def __str__(self):
        return  str(self.movie)


class cast(models.Model):
    movie=models.ForeignKey(movie,related_name='cast',on_delete=models.CASCADE)
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name
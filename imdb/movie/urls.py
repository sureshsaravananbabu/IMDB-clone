from django.urls import path
from .views import MovieList,MovieDetail,MovieCategory,MovieLanguage,MovieSearch,MovieYear,MostWatch
from django.conf.urls import url

 
app_name='movie'
urlpatterns = [
    path('', MovieList.as_view(),name='Movie_List'),
    path('category/<str:category>', MovieCategory.as_view(),name='MovieCategory'),
    path('language/<str:lang>', MovieLanguage.as_view(),name='MovieLanguage'),
    path('search/', MovieSearch.as_view(),name='MovieSearch'),
    path('<slug:slug>', MovieDetail.as_view(),name='Movie_Detail'),
    path('year/<int:year>', MovieYear.as_view(),name='MovieYear'),
    path('mostwatch/',MostWatch.as_view(),name='MostWatch')
]
from django.urls import path
from . import views
app_name = 'images'
urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/',
         views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path("ranking/", views.image_ranking, name="ranking"),
    path('', views.image_list, name='list'),
]


# http://localhost:8000/images/create/?title=%20Django%20and%20Duke&url=https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg

# http://localhost:8000/images/create/?title=%20Django%20and%20Duke&url=https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/18_Delphini.png/1024px-18_Delphini.png


# http://localhost:8000/images/create/?title=%20Django%20and%20Duke&url=https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/%22Shaman%22_rock.jpg/1280px-%22Shaman%22_rock.jpg


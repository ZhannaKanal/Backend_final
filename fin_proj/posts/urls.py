from django.urls import path
from . import views

from django.contrib import admin


urlpatterns = [
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('prices', views.prices, name='prices'),
    path('gallery', views.gallery, name='gallery'),
    path('signup', views.signup, name='signup'),
    path('order/', views.index, name='index'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    #path('hello', views.hello, name='hello'),
    path('post/<int:post_id>',views.show_id,name='post'),
    path('post/<slug:post_slug>',views.show_slug, name='posts'),
    path('show_post', views.show_post, name='show_post'),
    path('place/<slug:post_slug>', views.placesBySlug,name = 'place' )
   
]
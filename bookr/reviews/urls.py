from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name = 'welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book, name='book'),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/new/',views.publisher_edit, name='publisher_create'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:pk>/media/', views.book_media, name='book_media'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/',views.review_edit, name='review_edit'),
]

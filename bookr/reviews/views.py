from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Contributor, Publisher
from django.contrib import messages
from .utils import average_rating
from .form import PublisherForm, SearchForm

# Create your views here.

def index(request):
    return render(request, 'base.html')

def search(request):
    search = request.GET.get('search')
    return render(request, 'search.html', {'search':search})

def welcome_view(request):
    return render(request, 'base.html')

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book':book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    context = {
        'book_list': book_list
    }
    return render(request, 'book_list.html', context)

def book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if (reviews):
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            'book': book,
            'book_rating': book_rating,
            'reviews': reviews
        }
    else:
        context = {
            'book': book,
            'book_rating': None,
            'reviews': None
        }
    return render(request,'book.html',context)

def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
        
    if request.method == 'POST':
        form = PublisherForm(request.POS, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, 'Publisher \'{}\' was created.'.format(updated_publisher))
            else:
                messages.success(request, 'Publisher \'{}\' was updated'.format(updated_publisher))
        
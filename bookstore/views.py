# views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Genre, Reader, Book, Author, BookPromotion


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)


def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)


def book_promotion(request):
    books_with_promotion = Book.objects.exclude(promotion__isnull=True).order_by('title')
    print(books_with_promotion)
    context = {
        'books_with_promotion': books_with_promotion,
    }
    return render(request, 'book_promotion.html', context)


def book_promotion_list(request):
    books_with_promotion = BookPromotion.objects.select_related('book').order_by('book__title')
    context = {'books_with_promotion': books_with_promotion}
    return render(request, 'book_promotion_list.html', context)


def popular_authors_and_readers(request):
    popular_authors = Author.objects.annotate(num_readers=Count('books_written__readers')).order_by('-num_readers')
    author_reader_info = []
    for author in popular_authors:
        readers = Reader.objects.filter(books_read__author=author)
        author_reader_info.append({'author': author, 'readers': readers})
    context = {'author_reader_info': author_reader_info}
    return render(request, 'popular_authors_and_readers.html', context)


def unpopular_genres_and_readers(request):
    unpopular_genres = Genre.objects.annotate(num_readers=Count('books_in_genre__readers')).order_by('num_readers')
    genre_reader_info = []
    for genre in unpopular_genres:
        readers = Reader.objects.filter(books_read__genre=genre)
        genre_reader_info.append({'genre': genre, 'readers': readers})
    context = {'genre_reader_info': genre_reader_info}
    return render(request, 'unpopular_genres_and_readers.html', context)


def loyal_readers(request):
    queryReaders = Reader.objects.annotate(num_books=Count('books_read')).filter(num_books__gt=1)
    reader_info = []
    for reader in queryReaders:
        books = Book.objects.filter(readers=reader)
        reader_info.append({'reader': reader, 'books': books})
    context = {'reader_info': reader_info}
    return render(request, 'loyal_readers.html', context)
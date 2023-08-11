from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=120)


class Reader(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_written')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books_in_genre')
    readers = models.ManyToManyField(Reader, related_name='books_read')


class BookPromotion(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='promotion')

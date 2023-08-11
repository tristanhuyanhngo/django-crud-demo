from django.db import transaction
from faker import Faker
from bookstore.models import Author, Reader, Genre, Book, BookPromotion, Book2

fake = Faker()


@transaction.atomic
def run():
    # Tạo dữ liệu mẫu cho Author
    for _ in range(100):
        Author.objects.create(
            name=fake.name(),
            bio=fake.text(),
            birth_date=fake.date_of_birth(),
            nationality=fake.country()
        )

    # Tạo dữ liệu mẫu cho Reader
    for _ in range(100):
        Reader.objects.create(
            name=fake.name(),
            email=fake.email(),
            gender=fake.random_element(['M', 'F', 'O']),
            date_of_birth=fake.date_of_birth(),
            address=fake.address()
        )

    # Tạo dữ liệu mẫu cho Genre
    for _ in range(10):
        Genre.objects.create(
            name=fake.word(),
            description=fake.text()
        )

    # Tạo dữ liệu mẫu cho Book
    authors = Author.objects.all()
    genres = Genre.objects.all()
    readers = Reader.objects.all()

    for _ in range(100):
        author = fake.random_element(authors)
        genre = fake.random_element(genres)
        book = Book.objects.create(
            title=fake.catch_phrase(),
            publish_date=fake.date_between(start_date='-5y', end_date='today'),
            price=fake.random_element(elements=(10.0, 50.0)),
            author=author,
            genre=genre
        )
        book.readers.set(fake.random_elements(readers, length=fake.random_int(0, 10000)))

    # Tạo dữ liệu mẫu cho BookPromotion
    books = Book.objects.all().order_by('?')[:50]
    for book in books:
        BookPromotion.objects.create(
            code=fake.word(),
            discount_percentage=fake.random_element(elements=(10, 50)),
            start_date=fake.date_between(start_date='-1y', end_date='today'),
            end_date=fake.date_between(start_date='today', end_date='+1y'),
            book=book
        )

    # Tạo dữ liệu mẫu cho Book2
    for _ in range(100):
        author = fake.random_element(authors)
        genre = fake.random_element(genres)
        Book2.objects.create(
            title=fake.catch_phrase(),
            author_id=author.id,  # Sử dụng .id ở đây
            genre_id=genre.id,  # Sử dụng .id ở đây
            publish_date=fake.date_between(start_date='-5y', end_date='today'),
            price=fake.random_element(elements=(10.0, 50.0))
        )


if __name__ == "__main__":
    run()

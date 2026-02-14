from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books= models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def addBook( postData ):
    title = postData['book_title']
    desc = postData['book_desc']
    Book.objects.create(title=title, desc=desc)


def show_books():
    return Book.objects.all()

def book_details( id ):
    book = Book.objects.get(id=id)
    authors_of_book = book.authors.all()
    all_authors = Author.objects.all()
    all_authors = Author.objects.exclude(id__in=authors_of_book.values_list('id', flat=True))
    list ={
        'book_details' : Book.objects.get(id=id),
        'author': authors_of_book,
        'all_authors' : all_authors
    }
    return list


def add_author_to_book(book_id, author_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    book.authors.add(author)


def delete_book(id):
    book_to_delete = Book.objects.get(id= id['book_id'])
    book_to_delete.delete()

##########################

def add_author( postData ):
    first_name = postData['first_name']
    last_name = postData['last_name']
    notes = postData['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)


def show_authors():
    return Author.objects.all()

def author_details(id):
    author = Author.objects.get(id = id)
    books_of_author = author.books.all() 
    #execlude already exist authors if condition
    books_list = Book.objects.all()
    books_list = Book.objects.exclude(id__in=books_of_author.values_list('id', flat=True)) #id__in => id field of the book is in this list of values

    details = {
        'author_details' : author,
        'books_of_author' : books_of_author,
        'book' : books_list
    }
    return details


def add_book_to_author(author_id, book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = author_id)
    author.books.add(book)


def delete_author(author_id):
    author_to_delete = Author.objects.get(id=author_id)
    author_to_delete.delete()
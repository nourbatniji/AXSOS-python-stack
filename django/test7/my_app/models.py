from django.db import models
import bcrypt, re

# Create your models here.


class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')


        if len(postData['first_name']) < 3:
            errors['firstname_valid'] = 'First name must contain at least 3 characters'

        if len(postData['last_name']) < 3:
            errors['lastname_valid'] = 'Last name must contain at least 3 characters'
        
        #check email unique
        if get_email(postData['email']):
            errors['email_unique'] = 'Email already exists'

        if not email_regex.match(postData['email']):
            errors['email_valid'] = 'Invalid Email'

        if not pass_regex.match(postData['password']):
            errors['pass_valid'] = 'Invalid Password'

        if postData['password'] != postData['confirm_pw']:
            errors['matching'] = 'Passwords do not match'

        return errors
    
    def validate_login(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')

        #check email unique
        if not get_email(postData['email']):
            login_errors['login_email_unique'] = 'Email does not exist'

        if not email_regex.match(postData['email']):
            login_errors['login_email_valid'] = 'Invalid Email'

        if not pass_regex.match(postData['password']):
            login_errors['login_pass_valid'] = 'Invalid Password'

        return login_errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    #user_reviews
    #user_books
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #book_reviews


class Review(models.Model):
    rate = models.IntegerField()
    review = models.TextField()
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)


# CREATE USER
def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed_pw)


# GET USER EMAIL
def get_email(email):
    return User.objects.filter(email=email)


# GET USER BY ID
def get_id(id):
    return User.objects.get(id=id)


#CREATE BOOK
def create_book(postData):
    user = User.objects.get(id=postData['user_id'])
    author = Author.objects.get(id=postData['author_id'])
    book = Book.objects.create(title=postData['title'], user=user, author=author)
    Review.objects.create(review=postData['review'], rate=postData['rate'], user=user, book=book)

#GET ALL BOOKS
def get_all_reviews():
    return Review.objects.all()

# GET ALL AUTHORS / USERS:
# def get_all_authors():
#     return Book.objects.
from django.db import models
import bcrypt
import re

# Create your models here.


class UserManager(models.Manager):
    def reg_valid(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        if len(postData['username']) < 3 :
            errors['name_valid'] = 'User name should be at least 3 characters'
 
        if len(postData['alias']) < 3 :
            errors['alias_valid'] = 'Alias name should be at least 3 characters'

        if is_exist(postData['email']):
            errors['email_uniquness'] = 'Email already exists'

        if not email_regex.match(postData['email']):
            errors['email_valid'] = "Invalid email"
        
        if not pass_regex.match(postData['password']):
            errors['password_valid'] = "Invalid password"

        if postData['password'] != postData['confirm_pw']:
            errors['matching_valid'] = "Passwords do not match"

        return errors
        

class User(models.Model):
    username = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    objects = UserManager()
    #books
    #review

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45) 
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #review

class Review(models.Model):
    rate = models.IntegerField()
    review = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_user(postData): #DONE
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create(
        username=postData['username'],
        alias=postData['alias'],
        email=postData['email'],
        password=hashed_pw, 
    )

def get_user_byid(id):
    return User.objects.get(id=id)

def create_book(postData):
    this_user = User.objects.get(id=postData['user_id'])
    this_book = Book.objects.create(
        user=this_user,
        title=postData['title'],
        author=postData['author']
    )
    this_review = Review.objects.create(user=this_user, book= this_book, review=postData['review'], rate=postData['rate'])



def get_all_books():
    print(Book.objects.all())
    return Book.objects.all()

def get_book_byid(id):
    return Book.objects.filter(id=id)


def is_exist(data):
    return User.objects.filter(email=data)
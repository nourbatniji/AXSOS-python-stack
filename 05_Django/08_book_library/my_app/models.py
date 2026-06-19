from django.db import models
import bcrypt, re

# Create your models here.


class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex =  re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        if len(postData['first_name']) < 3:
            errors['firstname_valid'] = "First name must contain at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['lastname_valid'] = "Last name must contain at least 3 characters"
        if not email_regex.match(postData['email']):
            errors['email_valid'] = 'Invalid email'
        if not pass_regex.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 8 characters'
        if not pass_regex.match(postData['confirm_pw']):
            errors['confirm_pw_valid'] =  'Password confirmation must contain at least 8 characters'
        if postData['password'] != postData['confirm_pw']:
            errors['pass_match'] = 'Passwords do not match'
        return errors
    

    def validate_login(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex =  re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        if not email_regex.match(postData['email']):
            errors['email_valid'] = 'Invalid email'
        if not pass_regex.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 8 characters'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #uploaded by
    #liked_books
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)#user who uploaded a certain book
    liked_by = models.ManyToManyField(User, related_name='liked_books') #list of users




def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],email=postData['email'],password=hashed_pw)

def get_user_by_id(id):
    return User.objects.get(id= id)

def get_all_books():
    return Book.objects.all()

def get_book_by_id(id):
    return Book.objects.get(id= id)

def add_fav_book(postData):
    this_user = User.objects.get(id=postData['user_id'])
    this_book = Book.objects.create(title=postData['title'], desc=postData['desc'], uploaded_by=this_user)
    this_book.liked_by.add(this_user)

def add_book_to_fav(postData):
    this_user = User.objects.get(id=postData['user_id'])
    this_book = Book.objects.get(id=postData['book_id'])
    this_user.liked_books.add(this_book)

def get_user_likes(id):
    user = User.objects.get(id= id)
    return user.liked_books.all()

def update_book(postData):
    book = Book.objects.get(id=postData['book_id'])
    book.title = postData['title']
    book.desc = postData['desc']
    book.save()

def delete_book(postData):
    book = Book.objects.get(id=postData['book_id'])
    book.delete()
        
def del_from_fav(postData):
    book_to_delete = Book.objects.get(id=postData['book_id'])
    user_to_del_from = User.objects.get(id=postData['user_id'])
    user_to_del_from.liked_books.remove(book_to_delete)
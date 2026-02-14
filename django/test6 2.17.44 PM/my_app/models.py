from django.db import models
import bcrypt
import re

# Create your models here.

# 

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        if len(postData['first_name']) < 3:
            errors['firstname_valid'] = "First name should contain at least 3 characters"

        if not postData['first_name'].isalpha():
            errors['invalid_firstname'] = "First name should only be letters"

        if len(postData['last_name']) < 3:
            errors['lastname_valid'] = "First name should contain at least 3 characters"

        if not postData['last_name'].isalpha():
            errors['invalid_lastname'] = "Last name should only be letters"

        if is_exist(postData['email']) == True:
            errors['not_unique'] = "Email already exists"

        if not email_regex.match(postData['email']):
            errors['email_valid'] = "Invalid Email"

        if not pass_regex.match(postData['password']):
            errors['password_valid'] = "Passwrod should contain at least 3 characters"
        
        if postData['password'] != postData['confirm_pw']:
            errors['matching_valid'] = 'Passwords do not match'

        return errors
    
    def login_validator(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')


        if is_exist(postData['email']) == False:
            login_errors['not_unique'] = "Email does not exist"

        if not email_regex.match(postData['email']):
            login_errors['email_valid'] = "Invalid Email"

        if not pass_regex.match(postData['password']):
            login_errors['password_valid'] = "Passwrod should contain at least 3 characters"
        
        # if not check_pw(postData):
        #     login_errors['pass_not_correct'] = "Incorrect Passwrod"

        return login_errors
        




class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    #user_books
    #user_reviews
    objects=UserManager()

class Book(models.Model):
    title = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name='user_books', on_delete=models.CASCADE)
    #book_reviews


class Review(models.Model):
    review = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    review = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create(
        first_name=postData['first_name'],
        last_name=postData['last_name'],
        email=postData['email'],
        password=hashed_pw
    )




# check if email exist
def is_exist(email):
    return User.objects.filter(email=email).exists()


# def check_pw(postData):
#     user = get_user(postData['email'])
#     logged_user = user
#     for userr in user:
#         userr = user.passwer
        
#     print(user)
#     if bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
#         return True
#     else:
#         return False
    



   



#get user by email
def get_user(email):
    return User.objects.filter(email = email)


#get user by id
def get_user_by_id(id):
    return User.objects.get(id = id)
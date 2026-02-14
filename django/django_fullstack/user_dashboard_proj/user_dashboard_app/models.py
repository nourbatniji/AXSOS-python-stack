from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if not email_regex.match(postData['email']):
            errors['email_valid'] = "Invalid Email"
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name must contain at least 3 characters'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name must contain at least 3 characters'
        if not password_regex.match(postData['password']):
            errors['pass_valid'] = "Invalid Password, must contain at least 8 characters"
        if not password_regex.match(postData['confirm_pw']):
            errors['confirmPw_valid'] = "Invalid Confirm Password, must contain at least 8 characters"
        if postData['confirm_pw'] != postData['password']:
            errors['pass_match'] = "Passwords do not match"
        return errors
    

    def login_validation(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if not email_regex.match(postData['email']):
            login_errors['email_valid'] = "Invalid Email"

        if not password_regex.match(postData['password']):
            login_errors['pass_valid'] = "Invalid Password, must contain at least 8 characters"

        return login_errors

    

class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

# class Admin(models.Model)
#     user = 


def create_user(postData):
    email = postData['email']
    first_name = postData['first_name']
    last_name = postData['last_name']
    password = postData['password']
    confirm_pw = postData['confirm_pw']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    hashed_confirmPw = bcrypt.hashpw(confirm_pw.encode(), bcrypt.gensalt()).decode()
    User.objects.create(email=email, first_name=first_name, last_name=last_name, password=hashed_pw, confirm_pw=hashed_confirmPw)



def display_all_users():
    return User.objects.all()
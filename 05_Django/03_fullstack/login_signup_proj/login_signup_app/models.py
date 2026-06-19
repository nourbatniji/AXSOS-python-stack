from django.db import models
import re
import bcrypt
from django.utils import timezone
import datetime
from datetime import date



# Create your models here.

class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex =  re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')
        birthday_date = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()
        today = date.today()
        current_year = today.year

        if len(postData['first_name']) < 2:
            errors['firstname_valid'] = 'First name should contain at least  2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should contain at least  2 characters'

        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid Email'

        if not pass_regex.match(postData['password']):
            errors['password'] = 'Password must contain at least 8 characters'
        
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pass'] = 'Passwords do not match'

        if not (current_year - birthday_date.year) > 13 or current_year - birthday_date.year == 0:
            errors['coppa-compliant'] = "User has to be at least 13 years"
        
        if birthday_date > timezone.now().date():
            errors['birthday_valid'] = 'Invalid birthday'

        return errors
    
    def validate_login(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')

        if not email_regex.match(postData['email']):
            login_errors['email'] = "Invalid email"

        if not password_regex.match(postData['password']):
            login_errors['pass'] = "Password has to be at least 8 characters"

        return login_errors



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=190)
    confirm_pw = models.CharField(max_length=190)
    objects = UserManager()



def create_user(postData):
    first_name = postData['first_name']
    last_name = postData['last_name']
    birthday = postData['birthday']
    email = postData['email']
    password = postData['password']
    confirm_pw = postData['confirm_pw']

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    hased_confirm_pw = bcrypt.hashpw(confirm_pw.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=first_name, last_name=last_name, birthday=birthday, email=email, password=hashed_pw, confirm_pw=hased_confirm_pw)
    return user


def get_user_by_id(id):
    return User.objects.get(id=id)